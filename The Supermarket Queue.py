def queue_time(customers, n):
    def one_checkout(peoples):
        queue_time = 0
        for man in peoples:
            queue_time += man
        return queue_time

    def more_checkouts(peoples, n):
        customers_list = []
        for man in peoples:
            if len(customers_list) == n:
                index_min = customers_list.index(min(customers_list))
                customers_list[index_min] += man
                print(customers_list)
            else:
                customers_list.append(man)
                print(customers_list)
        return max(customers_list)

    if n == 1:
        return one_checkout(customers)
    else:
        return more_checkouts(customers, n)


customers = [1, 10, 2, 15, 17]
print(queue_time(customers, 2))