from src.common.find_locator import locators_dicts


def find_locator(element):
    for obj in locators_dicts.all_objects:
        for key, value in obj.items():
            if key == element:
                locator = value
                return locator
            else:
                continue
