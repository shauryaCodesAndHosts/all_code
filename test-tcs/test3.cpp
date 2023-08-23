#include <iostream>
using namespace std;
class RunDCode
{
    int x,y;
    public :
    RunDCode(int xx)
    {
        x=++xx;
    }
    ~RunDCode()
    {
        cout<<x-1<<" ";
    }
    void display()
    {
        cout<<--x+1<<" ";
    }
};
int main()
{
    RunDCode objCode(5);
    objCode.display();
    int *p=(int*)&objCode;
    *p=40;
    objCode.display();
    return 0;
}