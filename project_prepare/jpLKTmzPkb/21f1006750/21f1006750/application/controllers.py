from flask import request
from flask import render_template
from flask import current_app as app
from application.models import Category,Product, Customers, Managers, CustomerCart, CustomerOrders, SoldProductData
from .database import db
from flask import redirect 
from flask import url_for
from main import bcrypt
from sqlalchemy import func
import time
import matplotlib
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
#from .controllers import login_manager
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
#from flask_bcrypt import Bcrypt

#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view='customerLogin'

login_manager = LoginManager()
# allows our app to handle things like loggin in
login_manager.init_app(app)
login_manager.login_view='customerLogin'

now_user = None

@login_manager.user_loader
def load_Customer(customerId):
    return Customers.query.get(int(customerId))

#@login_manager.user_loader
#def load_Manager(managerId):
#    return Managers.query.get(int(managerId))



@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form['user-type'] == "manager":
            @login_manager.user_loader
            def load_Manager(managerId):
                return Managers.query.get(int(managerId))
            #login_manager.login_view='managerLogin'
            return redirect(url_for('managerLogin'))
        if request.form['user-type'] == "customer":
            @login_manager.user_loader
            def load_Customer(customerId):
                return Customers.query.get(int(customerId))
            #login_manager.login_view='customerLogin'
            return redirect(url_for('customerLogin'))
    if request.method == "GET":
        return render_template('startPage.html')

@app.route('/customerLogin',methods=['GET','POST'])
def customerLogin():
    if request.method == 'GET':
        return render_template('customerLogin.html')
    try:
        if request.method == 'POST':
            UserName = request.form['UserName']
            UserPassword = request.form['Password']
            print(UserName)
            print(UserPassword)
            password_hash = bcrypt.generate_password_hash(UserPassword).decode('utf8')
            print(password_hash)
            customer__original = Customers.query.filter_by(customerUserName = UserName).first()
            manager__original = Managers.query.filter_by(managerUserName = UserName).first()
            print(customer__original)
            if customer__original:
                #global now_user
                #now_user = customer__original
                print(customer__original.customerUserPassword)
                if  bcrypt.check_password_hash(customer__original.customerUserPassword, UserPassword):
                    login_user(customer__original)
                    print(current_user.customerId)
                    print(now_user)
                    return redirect(url_for('customerDashboard'))
                    return render_template('test.html',current_user=now_user)

                else:
                    return render_template('customerLogin.html')
            else:
                return render_template('customerLogin.html')
            if manager__original:
                if bcrypt.check_password_hash(manager__original.managerPassword,UserPassword):
                    login_user(manager__original)
                    return redirect(url_for('addCategory'))
    except TypeError:
        return redirect(url_for('customerLogin'))
        #if customerUserName == customer__original.customerUserName:
        #    print(customer__original.customerUserPassword)
        #    if bcrypt.check_password_hash(customer__original.customerUserPassword, customerUserPassword):
        #        print('its a fucking match')
        #        login_user(customer__original)
        #        print('testing')
        #        print(current_user)
        #        #current_user = customer__original
        #        return redirect(url_for('customerDashboard'))
        #return render_template('customerLogin.html')
        #print(managerUserName,managerUserName__original.managerUserName, managerPassword)
        #return redirect(url_for('customerLogin'))
   
@app.route('/customerSignUp',methods=['GET','POST'])
def customerSignUp():
    try:
        if request.method == 'POST':
            customerFirstName=request.form['customerFirstName']
            customerLastName= request.form['customerLastName']
            customerUserName = request.form['customerUserName']
            customerMailId = request.form["customerMailId"]
            customerUserPassword = request.form['customerUserPassword']
            hash_user_password = bcrypt.generate_password_hash(customerUserPassword).decode('utf8')
            customerAddress = request.form['customerAddress']
            customerCity = request.form['customerCity']
            customerState = request.form['customerState']
            new_customer = Customers(customerFirstName=customerFirstName,
                                     customerLastName=customerLastName,
                                     customerUserName = customerUserName,
                                     customerMailId = customerMailId,
                                     customerUserPassword = hash_user_password,
                                     customerAddress = customerAddress+", "+customerCity+", "+customerState
                                     )
            print(new_customer.customerAddress)
            db.session.add(new_customer)
            db.session.commit()
            return redirect(url_for('customerSignUp'))
        return render_template('customerSignUp.html')
    except : 
        return render_template('error.html')



@app.route('/customerDashboard/allCategories',methods=['GET','POST'])
@login_required
def allCategories():
    print('checking')
    #print(now_user)
    #print(now_user)
    all_categories = Category.query.all()
    print(all_categories)
    print(current_user)
    return render_template('allCategories.html',all_categories=all_categories)



@app.route('/customerDashboard',methods=['GET','POST'])
@login_required
def customerDashboard():
    if request.method == 'POST':
        quantity=request.form['quantity']
        categoryId=request.form['categoryId']
        productId = request.form['productId']
        category = Category.query.filter_by(categoryId= categoryId).first()
        product = Product.query.filter_by(productId = productId).first()
        print(categoryId,productId)
        print(category,quantity)
        if( product.inStock >= int(quantity) ):
            product.inStock = product.inStock - int(quantity)
            db.session.commit()
            new_cart = CustomerCart(itemAddedQuantity = int(quantity),
                                    customerId=current_user.customerId,
                                    productId = product.productId)
            db.session.add(new_cart)
            db.session.commit()
        #return "true"
        return redirect(url_for('customerDashboard'))
    #print(get_latest_products())
    print(get_latest_products()[0].category.categoryName)
    return render_template('dashboard.html',products = get_latest_products())


def get_latest_products():
    latest_products = Product.query.order_by(Product.timeOfEntry.desc()).limit(20).all()
    print(latest_products)
    if len(latest_products) == 0:
        return render_template('error.html')
    return latest_products


@app.route('/customerDashboard/<categoryName>',methods=['GET','POST'])
@login_required
def productInCategories(categoryName):
    print('as')
    category = Category.query.filter_by(categoryName=categoryName).first()
    print(category.product[0].category)
    return render_template('productsInCategories.html',category=category)


@app.route('/addToCart', methods=["GET",'POST'])
@login_required
def addToCart():
    if request.method == 'POST':
        quantity=request.form['quantity']
        categoryId=request.form['categoryId']
        productId = request.form['productId']
        category = Category.query.filter_by(categoryId= categoryId).first()
        product = Product.query.filter_by(productId = productId).first()
        print(categoryId,productId)
        print(category,quantity)
        if( product.inStock >= int(quantity) ):
            product.inStock = product.inStock - int(quantity)
            db.session.commit()
            new_cart = CustomerCart(itemAddedQuantity = int(quantity),
                                    customerId=current_user.customerId,
                                    productId = product.productId)
            db.session.add(new_cart)
            db.session.commit()
        #return "true"
        return redirect(url_for('productInCategories',categoryName=category.categoryName))



@app.route('/displayCart/<cartItemId>',methods=['GET'])
@login_required
def deleteProductFromCart(cartItemId):
    item = CustomerCart.query.filter_by(cartItemId=cartItemId).first()
    print(item)
    item.product.inStock = item.product.inStock + item.itemAddedQuantity
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('displayCart'))
    pass


@app.route('/displayCart',methods=['GET','POST'])
@login_required
def displayCart():
    print(current_user.customerId)
    currentUserCart = CustomerCart.query.filter_by(customerId=current_user.customerId).all()
    total = 0
    for item in currentUserCart:
        total = total + (item.itemAddedQuantity*item.product.ratePerUnit)
    #print(currentUserCart[0].product.productName)
    print(total)
    return render_template('displayCart.html',cart_items=currentUserCart,total= total)


@app.route('/customerLogout',methods=['GET','POST'])
@login_required
def customerLogout():
    logout_user()
    return redirect(url_for('home'))


def OrderTotal(currentUserCart):
    total = 0
    for item in currentUserCart:
        total = total + (item.itemAddedQuantity*item.product.ratePerUnit)
    return total


def OrderTotalItems(currentUserCart):
    total = 0
    for item in currentUserCart:
        total = total + item.itemAddedQuantity
    return total

def listOfOrders(currentUserCart):
    names=''
    quantity=''
    for item in currentUserCart:
        names=names+item.product.productName+', '
        quantity= quantity+str(item.itemAddedQuantity)+", "
    return names, quantity



@app.route('/placeOrder',methods=['GET','POST'])
@login_required
def placeOrder():
    items_in_cart = CustomerCart.query.filter_by(customerId=current_user.customerId).all()
    l, q = listOfOrders(items_in_cart)
    diagnostic_data(items_in_cart=items_in_cart)
    if OrderTotal(items_in_cart) == 0:
        return redirect(url_for('displayCart'))
    new_order = CustomerOrders( orderTotal= OrderTotal(items_in_cart),
                               numberOfItems = OrderTotalItems(items_in_cart),
                                customerId=current_user.customerId,
                                listOfItems = l,
                                quantityOfItems = q
                                  )
    db.session.add(new_order)
    for item in items_in_cart:
        db.session.delete(item)
    db.session.commit()
    print('line 282')
    print(items_in_cart)
    return redirect(url_for('displayCart'))



def diagnostic_data(items_in_cart):
    print(items_in_cart)
    #sold=SoldProductData.query.filter_by(soldProductName = )
    for item in items_in_cart:
        if SoldProductData.query.filter_by(soldProductName = item.product.productName ).first() :
            temp = SoldProductData.query.filter_by(soldProductName = item.product.productName).first()
            temp.soldProductFreq = temp.soldProductFreq + item.itemAddedQuantity
        else:
            temp=SoldProductData(soldProductName = item.product.productName ,
                                 soldProductFreq = item.itemAddedQuantity,
                                 timeOfSelling = time.time())
            db.session.add(temp)
        db.session.commit()
    return render_template('error.html')



@app.route('/yourOrders',methods=['GET',"POST"])
@login_required
def yourOrders():
    orders = CustomerOrders.query.filter_by(customerId=current_user.customerId).all()
    print(orders)
    return render_template('yourOrders.html',orders=orders)



@app.route('/searchResult',methods=['GET','POST'])
@login_required
def searchResult():
    if request.method =='POST':
        #products = Product.query.filter(Product.name.like(f"%{keyword}%")).all()
        query=request.form['query']
        print(query)
        products = Product.query.filter(Product.productName.like(f"%{query}%")).all()
        print(products)
        return render_template('searchedProducts.html',products= products)
    



@app.route('/managerLogin/',methods=['GET',"POST"])
def managerLogin():
    try:
        if request.method == 'GET':
            return render_template('loginPage.html')
        if request.method == 'POST':
            managerUserName = request.form['managerUserName']
            managerPassword = request.form['managerPassword']
            password_hash = bcrypt.generate_password_hash(managerPassword).decode('utf8')
            print(password_hash)
            managerUserName__original = Managers.query.filter_by(managerUserName=managerUserName).first()
            if managerUserName == managerUserName__original.managerUserName:
                print(managerUserName__original.managerPassword)
                if bcrypt.check_password_hash(managerUserName__original.managerPassword, managerPassword):
                    login_user(managerUserName__original)
                    print(current_user)
                    return redirect(url_for('addCategory'))
            print(managerUserName,managerUserName__original.managerUserName, managerPassword)
            return render_template('loginPage.html')
    except AttributeError:
        return render_template('loginPage.html')
   

@app.route('/managerLogout', methods=['GET','POST'])
@login_required
def managerLogout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/addCategory',methods=["GET","POST"])
@login_required
def addCategory():
    if request.method == "POST":
        #print('in ifelse')
        categoryName= request.form['categoryName']
        #print(categoryName)
        newCategory = Category(categoryName = categoryName)
        #print(newCategory)
        db.session.add(newCategory)
        db.session.commit()
        all_categories = Category.query.all()
        #print(all_categories[0].categoryName)
        return redirect(url_for('addCategory'))

    all_categories = Category.query.all()
    print(all_categories[0].categoryName)
    return render_template('addCategory.html',allCategories = all_categories)


@app.route('/addProduct/<categoryName>',methods=['GET','POST'])
@login_required
def addProduct(categoryName):
    if request.method == "GET" :
        category = Category.query.filter_by(categoryName=categoryName).first()
        print(category)
        category = Category.query.get(category.categoryId)
        print(category)
        products = category.product
        for val in products:
            print(val.productName)
        return render_template('displayProducts.html',categoryName=categoryName,products=products)
    if request.method == "POST" :
        productName = request.form['productName']
        expiryDate = request.form['expiryDate']
        manufacturingDate = request.form['manufacturingDate']
        ratePerUnit = request.form['ratePerUnit']
        inStock= request.form['inStock']
        category = Category.query.filter_by(categoryName=categoryName).first()

        newProduct = Product(productName=productName,expiryDate=expiryDate,
                             manufacturingDate=manufacturingDate,ratePerUnit=float(ratePerUnit),
                             categoryId=category.categoryId,inStock=inStock,timeOfEntry = time.time())
        
        print(productName)
        #newProduct = Product(productName='test',expiryDate='23/23/2333',
        #                     manufacturingDate='23/42/5211',ratePerUnit=23.00,
        #                     categoryId=2)
        db.session.add(newProduct)
        db.session.commit()
        #print(newProduct.category.categoryName)
        return redirect(url_for('addProduct',categoryName=categoryName))
        return render_template('displayProducts.html',categoryName=categoryName)
    

@app.route('/updateProduct/<categoryName>/<productName>',methods=['GET','POST'])
@login_required
def updateProduct(categoryName,productName):
    if request.method == "GET":
        category = Category.query.filter_by(categoryName=categoryName).first()
        product= Product.query.filter_by(productName=productName,categoryId=category.categoryId).first()
        print(category)
        print(product)
        return render_template('editProduct.html',categoryName=categoryName,productName=productName)
    if request.method == "POST":
        category = Category.query.filter_by(categoryName=categoryName).first()
        product= Product.query.filter_by(productName=productName,categoryId=category.categoryId).first()
        if request.form['productName'] != '':
            product.productName = request.form['productName']
        if request.form['expiryDate'] != '':
            product.expiryDate = request.form['expiryDate']
        if request.form['manufacturingDate'] != '':
            product.manufacturingDate = request.form['manufacturingDate']
        if request.form['ratePerUnit'] != '':
            product.ratePerUnit = request.form['ratePerUnit']
        if request.form['inStock'] != '':
            product.inStock = request.form['inStock']
        db.session.commit()
        return redirect(url_for('addProduct',categoryName=categoryName))
        return render_template('editProduct.html',categoryName=categoryName,productName=productName)
        #category = Category.query.filter_by(categoryName=categoryName).first()


@app.route('/delete/<categoryName>',methods=['GET'])
@login_required
def deleteCategory(categoryName):
    category_obj=Category.query.filter_by(categoryName=categoryName).first()
    print(category_obj.categoryName)
    db.session.delete(category_obj)
    db.session.commit()
    return redirect(url_for('addCategory'))
    return render_template('test.html')


@app.route('/delete/<categoryName>/<productName>',methods=['GET'])
@login_required
def deleteProduct(categoryName,productName):
    category = Category.query.filter_by(categoryName=categoryName).first()
    product= Product.query.filter_by(productName=productName,categoryId=category.categoryId).first()
    print(product)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('addProduct',categoryName=categoryName))



matplotlib.use('agg')
# using because we dont need gui and it just write the image 

@app.route('/performanceOfProducts',methods=['GET','POST'])
@login_required
def performanceOfProducts():
    n=10
    count = 10
    if request.method=='POST':
        if request.form.get('numberOfEntries'):
            n=int(request.form['numberOfEntries'])
        elif request.form.get('numberOfCustomers'):
            count=int(request.form['numberOfCustomers'])
    products = SoldProductData.query.order_by(SoldProductData.soldProductFreq.desc()).limit(n).all()
    products_list = []
    quantity_list = []
    time_list = []
    for prod in products:
        products_list.append(prod.soldProductName)
        quantity_list.append(prod.soldProductFreq)
        time_list.append(prod.timeOfSelling)
    print(products_list)
    print(quantity_list)
    print(time_list)
    plt.barh(products_list,quantity_list,label='Quantity')
    plt.xlabel('Quantity')
    plt.ylabel('Product')
    plt.title('The overall performance of products')
    plt.legend()
    plt.savefig('./static/horizontal_bar_graph.png', bbox_inches='tight')
    plt.clf()

    active_customers = (
    db.session.query(CustomerOrders.customerId, func.count(CustomerOrders.orderId).label('order_count'))
    .group_by(CustomerOrders.customerId)
    .order_by(func.count(CustomerOrders.orderId).desc())
    .limit(count)  # You can adjust the limit as needed
    .all()
    )
    print('i need a job')
    customerName = []
    number_of_orders = []
    for c in active_customers:
        customerName.append((Customers.query.filter_by(customerId = c[0]).first()).customerUserName)
        number_of_orders.append(c[1])
    print(customerName)
    print(active_customers)
    plt.barh(customerName,number_of_orders,label='Quantity')
    plt.xlabel('Customer User Name')
    plt.ylabel('Number of Orders')
    plt.title('The overall performance of the Customers')
    plt.legend()
    plt.savefig('./static/horizontal_bar_graph_customers.png', bbox_inches='tight')
    plt.clf()

    return render_template('diagnostic.html')

