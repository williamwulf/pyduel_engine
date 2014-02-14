
class MenuLoader:

    def __init__(self, menu, cursor='> '):
        self.menu = menu
        self.cursor = cursor

    def load_menu(self):

        while True:
            print(self.menu['question'])
            print(30 * '-')
            for index, player_choice in enumerate(self.menu['choices']):
                print('{0}. {1}'.format(index + 1, player_choice))
            print(30 * '-')
            try:
                answer = int(input(self.cursor)) - 1
            except ValueError:
                print('Invalid input. Enter a value between 1-{0}'.format(
                    len(self.menu['choices'])))
                continue

            if not answer in range(0, len(self.menu['choices'])):
                print('Invalid input. Enter a value between 1-{0}.'.format(
                    len(self.menu['choices'])))
                continue

            return answer

    def load_enum_menu(self):

        while True:
            print(self.menu['question'])
            print(30 * '-')
            for player_choice in self.menu['choices']:
                print("{0}. {1}".format(player_choice['type'] + 1,
                                        player_choice['choice']))
            print(30 * '-')
            try:
                answer = int(input(self.cursor)) - 1
            except ValueError:
                print('Invalid input. Enter a value between 1-{0}'.format(
                    len(self.menu['choices'])))
                continue

            if not answer in range(0, len(self.menu['choices'])):
                print('Invalid input. Enter a value between 1-{0}.'.format(
                      len(self.menu['choices'])))
                continue

            return answer


if __name__ == '__main__':
    # action_menu = menu_loader(menus.CHOOSE_BOARD)
    # choice = action_menu.load_enum_menu()
    # print(choice)
    pass
