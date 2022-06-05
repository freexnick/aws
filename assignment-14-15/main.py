from operator import add
from create_user import create_user
from create_group import create_group
from add_user_to_group import add_user_to_group
from attach_group_policy import attach_group_policy
from create_login_profile import create_login_profile


def main():
    user_name = create_user("user_name")
    create_login_profile(user_name)
    group_name = create_group("group_name")
    attach_group_policy(group_name, "policy_name")
    add_user_to_group(user_name, group_name)


if __name__ == '__main__':
    main()
