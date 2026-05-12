from song import Song
import analytics
import parser
import inquirer

questions_main = [
    inquirer.Text('history_path', message='Directory with history data', default='history'),
    inquirer.List('analysis_type', message='What would you want to analyze?', choices=['Match song name / artist / album']),
    inquirer.Confirm('exit', message='Would you like to exit?', default=True),
]

def run():
    print('Spotify History Analist')

    answers = inquirer.prompt([questions_main[0]])
    path = answers['history_path']

    print('Loading data...')
    songs = parser.read_history(path)
    
    while True:
        answers = inquirer.prompt([questions_main[1]])

        analysis_type = answers['analysis_type']

        if analysis_type == 'Match song name / artist / album':
            match_songs(songs)

        answers = inquirer.prompt([questions_main[2]])
        if answers['exit']:
            break

    

questions_match = [
    inquirer.Text('query', message='Enter song name, artist or album'),
    inquirer.Confirm('sort_by_count', message='Do you want to sort songs by listening count?', default=True),
]

def match_songs(songs: list[Song]):
    counter = analytics.Counter(songs)

    answers = inquirer.prompt(questions_match)

    matched = counter.match(answers['query'])

    if answers['sort_by_count']:
        matched = analytics.Counter.count_sort(matched)

    matched = matched[:50]

    print(f'{len(matched)} matches!\n')
    analytics.Counter.count_print(matched)