# Copyright (c) 2018 Ainnovation.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2020/6/2
"""
"""

import htpasswd

with htpasswd.Basic("/Users/administrator/workspace/pycharm/python3_soup/htpasswd_t/user.db", mode="md5") as userdb:
    try:
        userdb.add("admin", "admin123")
    except htpasswd.basic.UserExists as e:
        print(e)

    # try:
    #     userdb.change_password("alice", "newpassword")
    # except htpasswd.basic.UserNotExists as e:
    #     print(e)

# with htpasswd.Group("/Users/administrator/workspace/pycharm/python3_soup/htpasswd_t/group.db") as groupdb:
#     try:
#         groupdb.add_user("admin1222", "admin123")
#     except htpasswd.group.UserAlreadyInAGroup as e:
#         print(e)

#     try:
#         groupdb.delete_user("alice", "managers")
#     except htpasswd.group.UserNotInAGroup, e:
#         print
#         e
