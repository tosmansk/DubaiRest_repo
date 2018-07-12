from lxml import html
from phptravels_utils.some_useful_utils import Logger


class HtmlParser(Logger):
    """This class makes parsing of HTML string data"""

    def __init__(self):
        super(HtmlParser, self).__init__('../phptravels_logs/utils.log')

    def find_element(self, content, element, el_type, obtain=None):
        """This class finds element based on its locator element"""

        html_content = html.fromstring(content)
        element_type = el_type
        locator = element
        found_elements = []


        if element_type == "class":
            found_element = html_content.find_class(locator)
        elif element_type == "xpath":
            found_element = html_content.xpath(locator)
        elif element_type == "css":
            found_element = html_content.cssselect(locator)
        elif element_type == "id":
            found_element = html_content.get_element_by_id(locator, default=None)

        # Obtain text, name from elements found
        for elements in range(len(found_element)):
            if obtain == 'text' and found_element is not None:

                text_found = found_element[elements].text.strip()
                self.log.info("Elememnt {0} with text: \"{1}\" found.".format(elements, text_found))
                found_elements.append(text_found)
            elif obtain == "name" and found_element is not None:
                name_found = found_element[elements].name
                self.log.info("Elememnt {0} with name: \"{1}\" found.".format(elements, name_found))
                found_elements.append(name_found)

        return found_elements









