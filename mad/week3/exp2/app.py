from jinja2 import Template
dict_data = [
    {'year': 1990, 'awardees': 'dr chutiya', 'language': 'bengali'},
    {'year': 1992, 'awardees': 'dr chutiya2', 'language': 'bengali2'},
    {'year': 1993, 'awardees': 'dr chutiya3', 'language': 'bengali3'}
]


def main():
    template_file = open('template.html')
    TEMPLATE = template_file.read()
    template_file.close()

    template = Template(TEMPLATE)
    htmlContent = template.render(dict_data=dict_data)

    new_html_document = open('new_template.html', 'w')
    new_html_document.write(htmlContent)
    new_html_document.close()


if __name__ == "__main__":
    main()
