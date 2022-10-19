def main():
    def create_deep_copy(struct, product):
        if isinstance(struct, dict):
            return {
                key: create_deep_copy(val, product)
                if key != "h2" and key != "title"
                else val.format(new_product=product)
                for key, val in struct.items()
            }

        return struct

    sites_num = int(input("Сколько сайтов? "))

    all_sites = {}
    for _ in range(sites_num):
        current_product = input("Какой продукт? ")
        all_sites[current_product] = create_deep_copy(site, current_product)

        for name_product, value_product in all_sites.items():
            print("Сайт для {0}: ".format(name_product), end=" ")
            print(value_product)


main()
