from InquirerPy import prompt
from InquirerPy.separator import Separator

from view.abstract_view import AbstractView
from view.session import Session

from services.pokemon_service import PokemonService
from services.battle_service import BattleService


class PokemonListView(AbstractView):
    def __init__(self):
        pokemon_list = []
        for i in range(30):
            pokemon_list.append(
                pokemon_service.get_pokemon_with_identifier_from_webservice(i)
            )
        pokemon_list.append("Retour")

        self.__question = [
            {
                "type": "list",
                "message": "Select Pokemon to get details",
                "choices": pokemon_list,
            }
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}, look at all those monsters ! Pick one !")

    def make_choice(self):
        answer = prompt(self.__question)

        if answer != "Retour":
            return PokemonDetailsView(answer)

        else:
            from view.start_view import StartView

            return StartView()
