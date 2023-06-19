import json
from datetime import datetime

#Reading the JSON file

fd = open('stops-Jan2023.json', 'r', encoding='utf-8')
read_data = json.load(fd)

# 1. Total number of incidents during the month
def total_incident():
    total_incidents = len(read_data)
    print(f'Total stop and search incidents: {total_incidents}')


# 2. Number of types searches
person_search  = []
person_Vehicle_search = []
vehicle_search = []

def type_search():
    for search in read_data:
        if search['type'] == 'Person search':
            person_search.append(search)
        elif search['type'] == 'Vehicle search':
            vehicle_search.append(search)
        else:
            person_Vehicle_search.append(search)

    print(f'Person search:{len(person_search)} ')
    print(f'Vehicle search:{len(vehicle_search)} ')
    print(f'Person and vehicle search: {len(person_Vehicle_search)} ')


# 3. Number of gender searches

male  = []
female = []

def gender_search():
    for search in read_data:
        if search['gender'] == 'Male':
            male.append(search)
        else:
            female.append(search)
    print(f'Men: {len(male)}')
    print(f'Female {len(female)} ')


#4. Total number of incidents based on the age range of person

eighten_twenty_four = []
twenty_five_thirty_four = []
over =[]
null = []

def age_search():
    for search in read_data:
        if search['age_range'] == '18-24':
            eighten_twenty_four.append(search)
        elif search['age_range'] == '25-34':
            twenty_five_thirty_four.append(search)
        elif search['age_range'] == 'over 34':
            over.append(search)
        else:
            null.append(search)

    print(f'Between 18-24: {len(eighten_twenty_four)} ')
    print(f'Between 25-34: {len(twenty_five_thirty_four)} ')
    print(f'Over 34: {len(over)} ')
    print(f'Not recorded: {len(null)} ')

#5.Total number of incidents based on day of week
day_of_week = {
    'Sunday': 0,
    'Monday': 0,
    'Tuesday': 0,
    'Wednesday': 0,
    'Thursday': 0,
    'Friday': 0,
    'Saturday': 0
}

def day_of_the_week():
    for search in read_data:
        datetime_search = search['datetime']
        datetime_strp = datetime.strptime(datetime_search, "%Y-%m-%dT%H:%M:%S%z")
        day = datetime_strp.strftime("%A")
        day_of_week[day] += 1
    print(day_of_week)


#6. The reason the stop and search was carried out

offensive_weapons =  []
article_for_use_in_theft = []
controlled_drugs = []
evidence_of_offences = []
stolen_goods = []
none = []
firearms = []

def object_of_search():
    for search in read_data:
        if search['object_of_search'] == 'Offensive weapons':
            offensive_weapons.append(search)
        elif search['object_of_search'] == 'Article for use in theft':
            article_for_use_in_theft.append(search)
        elif search['object_of_search'] == 'Controlled drugs':
            controlled_drugs.append(search)
        elif search['object_of_search'] == 'Evidence of offences under the Act':
            evidence_of_offences.append(search)
        elif search['object_of_search'] == 'Stolen goods':
            stolen_goods.append(search)
        elif search['object_of_search'] == 'Firearms':
            firearms.append(search)
        else:
            none.append(search)

    print(f'Offensive_weapons:{len(offensive_weapons)} ')
    print(f'Article_for_use_in_theft: {len(article_for_use_in_theft)}')
    print(f'Controlled_drugs: {len(controlled_drugs)}')
    print(f'Evidence_of_offences:{len(evidence_of_offences)}')
    print(f'Stolen_goods: {len(stolen_goods)}')
    print(f'None:{len(none)}  ')
    print(f'FireArms:{len(firearms)}')




if __name__ == '__main__':
    total_incident()
    print('*' * 36)
    type_search()
    print('*' * 30)
    gender_search()
    print('*' * 30)
    age_search()
    print('*' * 30)
    object_of_search()
    print('*' * 30)
    day_of_the_week()








