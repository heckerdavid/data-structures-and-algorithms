def zip_lists(list_1, list_2):
    follower_1 = list_1.head
    follower_2 = list_2.head
    leader_1 = follower_1.next
    leader_2 = follower_2.next

    while follower_1.next and follower_2.next:
        follower_1.next = follower_2
        follower_2.next = leader_1

        follower_2 = leader_2
        leader_2 = leader_2.next

        follower_1 = leader_1
        leader_1 = leader_1.next
    if follower_2:
        follower_1.next = follower_2
    if leader_1:
        follower_2.next = leader_1

    return list_1
