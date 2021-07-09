from typing import Tuple, Dict, Optional


class Pastrami:

    def __init__(self, bread: str = "rye"):
        self.bread: str = bread
        self.condiments: Tuple[str, str, str, str] = tuple()
        self.veggies: Tuple[str, str, str] = tuple()

    def add_condiments(self, conds: Tuple[str, str, str, str]) -> None:

        return None

    def add_veggies(self, veggies: Tuple[str, str, str]) -> None:
        setattr(self, "veggies", veggies)

        return None


class PastramiMaker:

    def __init__(self):
        self.p: Optional[Pastrami] = None

    @property
    def __str__(self):
        cond_string = ", ".join(self.p.condiments)
        veggie_string = ", ".join(self.p.veggies)

        return f"Got a hot pastrami here with {cond_string} and {veggie_string} on {str(self.p.bread)}"

    def make_sandwich(self, user_choices: Dict[str: Tuple[str, ..., str]]) -> None:
        """
        make the pastrami sandwich order
        :param user_choices:
        :return: None
        """

        self.p.add_condiments(user_choices['conds'])
        self.p.add_veggies(user_choices['veggies'])

        return None
