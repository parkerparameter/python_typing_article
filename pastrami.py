class Pastrami:

    def __init__(self, bread: str = "rye"):

        self.bread: str = bread
        self.condiments: tuple = tuple()
        self.veggies: tuple = tuple()

    def add_condiments(self, conds: tuple) -> None:
        """
        setter for self.condiments
        :param conds: tuple condiments to spread on sandwich
        :return:
        """

        setattr(self, "condiments", conds)

        return None

    def add_veggies(self, veggies: tuple):
        """
        setter for self.veggies
        :param veggies: tuple of veggies
        :return:
        """
        setattr(self, "veggies", veggies)

        return None


class PastramiMaker:

    def __init__(self):

        self.p: Pastrami = None

    def __order_up__(self, bread: str = "rye"):
        """
        create order for new pastrami sandwich
        setter for self.p
        :param bread: str bread for sandwich
        :return: none
        """

        setattr(self, "p", Pastrami(bread=bread))

        return None

    @property
    def __str__(self):
        cond_string = ", ".join(self.p.condiments)
        veggie_string = ", ".join(self.p.veggies)

        return f"Got a hot pastrami here with {cond_string} and {veggie_string} on {str(self.p.bread)}"

    def make_sandwich(self, user_choices: dict):
        """
        make the pastrami sandwich order
        :param user_choices:
        :return: None
        """

        self.p.add_condiments(user_choices['conds'])
        self.p.add_veggies(user_choices['veggies'])

        return None