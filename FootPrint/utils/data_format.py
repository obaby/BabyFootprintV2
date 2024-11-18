def format_user_info(user):
    return {'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'nick_name': user.userextendinfo.nick_name if user.userextendinfo else None,
            'sex': user.userextendinfo.sex if user.userextendinfo else None,
            'avatar': user.userextendinfo.avatar if user.userextendinfo else None,
            'is_email_confirmed': user.userextendinfo.is_email_confirmed if user.userextendinfo else None,
            'mobile': user.userextendinfo.mobile if user.userextendinfo else None,
            'age': user.userextendinfo.age if user.userextendinfo else None,
            'menstrual_cycle': user.userextendinfo.menstrual_cycle if user.userextendinfo else None,
            'menstrual_days': user.userextendinfo.menstrual_days if user.userextendinfo else None,
            'last_menstruation_date': user.userextendinfo.last_menstruation_date if user.userextendinfo else None,
            'is_can_be_find': user.userextendinfo.is_can_be_find,
            'is_can_add_to_lover': user.userextendinfo.is_can_add_to_lover,
            'create': user.userextendinfo.create,
            'update': user.userextendinfo.update,
            'height': user.userextendinfo.height,
            'birthday': user.userextendinfo.birthday,
            }


def calc_bmi(user, weight):
    if user.userextendinfo.height and weight:
        return round(weight / ((user.userextendinfo.height / 100) ** 2), 2)
    return None


if __name__ == "__main__":
    print('data test')
