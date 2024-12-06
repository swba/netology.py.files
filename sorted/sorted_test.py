from sorted import sort_files
from os import getcwd, path

def test_sort_files():
    # Create a file.
    sort_files()
    # Open it and check if its content is correct.
    with open(path.join(getcwd(), 'files', 'sorted.txt'), encoding='UTF-8') as file:
        assert file.read() == ('2.txt\n1\n'
                               'Тревога началась в тринадцать часов ноль две минуты.\n'
                               '1.txt\n8\n'
                               'Начальник  полиции\n'
                               'лично позвонил в шестнадцатый участок. А спустя  одну минуту тридцать секунд\n'
                               'в дежурке и других комнатах нижнего этажа раздались звонки\n'
                               '     Когда Иенсен  --  комиссар  шестнадцатого  участка --  вышел  из своего\n'
                               'кабинета,  звонки еще  не смолкли. Иенсен был мужчина средних лет,  обычного\n'
                               'сложения, с лицом плоским и невыразительным. На последней ступеньке винтовой\n'
                               'лестницы  он задержался  и  обвел взглядом помещение дежурки. Затем поправил\n'
                               'галстук и проследовал к машине.\n'
                               '3.txt\n9\n'
                               '     В  это время  дня  машины текли сплошным  блестящим  потоком,  а  среди\n'
                               'потока, будто  колонны из бетона  и стекла, высились  здания. Здесь,  в мире\n'
                               'резких граней,  люди  на тротуарах  выглядели  несчастными и  неприкаянными.\n'
                               'Одеты они были хорошо, но как-то удивительно походили друг на друга и все до\n'
                               'одного спешили. Они шли нестройными  вереницами, широко разливались, завидев\n'
                               'красный  светофор или  металлический  блеск кафе-автоматов.  Они непрестанно\n'
                               'озирались по сторонам и теребили портфели и сумочки.\n'
                               '     Полицейские  машины  с  включенными  сиренами  пробивались  сквозь  эту\n'
                               'толчею.\n')