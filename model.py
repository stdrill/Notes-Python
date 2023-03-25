import csv


def write_notes(notes):
    with open('notes.csv','w',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=['id','title','body','created_at','update_at'], delimiter=',')
        writer.writeheader()
        for note in notes:
            writer.writerow(note)


def read_notes():
    notes = []
    with open('notes.csv','r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            row['id'] = int(row['id'])
            notes.append(row)
        if not notes:
            print("Список пуст")
    return notes

