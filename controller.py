import model as m
import datetime


def add_note():
    notes = m.read_notes()
    max_id = max([note['id'] for note in notes]) if notes else 0
    new_note = {
        'id': max_id + 1,
            'title':input('Введите заголовок: '),
            'body': input('Введите текст: '),
            'created_at':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'update_at':''
    }
    notes.append(new_note)
    m.write_notes(notes)


def delete_note():
    notes = m.read_notes()
    note_id = int(input('Введите id заметки: '))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            break
    else:
        print('Заметка не найдена')
    m.write_notes(notes)


def edit_note():
    notes = m.read_notes()
    note_id = int(input('Введите id заметки:'))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input('Введите новый заголовок: ')
            note['body'] = input('Введите новый текст: ')
            note['update_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            break
    else:
        print('Заметка не найдена')
    m.write_notes(notes)


def read_notes_filter():
    from_date = datetime.datetime.strptime(
        input('Введите дату/время в формате ГГГГ-ММ-ДД ЧЧ:ММ: '), '%Y-%m-%d %H:%M')
    notes = m.read_notes()
    notes_filter = [note for note in notes if datetime.datetime.strptime(note['created_at'], '%Y-%m-%d %H:%M:%S')
                    >= from_date or note['updated_at'] and datetime.datetime.strptime(note['updated_at'], '%Y-%m-%d %H:%M:%S') >= from_date]
    return notes_filter
