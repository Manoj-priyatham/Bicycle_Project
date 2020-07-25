import json
import collections


def item_price(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(item_price(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))

    return dict(items)


def main():
    jp = open('bicycle_input.json')
    price_dict = json.load(jp)
    final_price = {}
    total = 0
    print('{:25}{}'.format('ITEM', 'VALUE'))
    print('--------------------------------------------')
    for k, v in price_dict.items():
        res = sum([int(i) for i in item_price(v).values()])
        total += res
        print("{:25}{}".format(k, res))
        final_price.update({k: res})
    print('--------------------------------------------')
    print('{:25}{}'.format('TOTAL', total))
    final_price.update({'total': total})

    return final_price


if __name__ == '__main__':
    main()