from django.shortcuts import render
from member.models import Member
from flightlog.forms import CreateTripForm

def home(request):
    news = [
        {           
            'weight': 5,
            'contenttype': 'video',
            'datas': 
                {
                    'provider': 'youtube',
                    'title': 'New Icepeak 8',
                    'desc': 'Niviuk presents his new EN D wing',
                    'provider_id': '53MsjUi1F_E',
                },
        },
        {
            'weight': 4.3,
            'contenttype': 'flightlog',
            'datas':
                {
                    'pilot': Member.objects.all()[0],
                    'date':'2015-04-08T02:49:49.216456',
                    'take_off': 'Chorges',
                    'landing': 'Chorges',
                    'track': [],
                    'gear': 
                        [
                            {
                                'gear_type': 'Parapente',
                                'name': 'AirDesign Rise M'
                            }
                        ],
                }
        },
        {
            'weight': 4,
            'contenttype': 'picture',
            'datas': 
                {
                    'provider': 'flickr',
                    'provider_id': 'https://farm8.staticflickr.com/7090/7256200554_6011c937eb_o_d.jpg',
                    'title': 'Spring at Woodside',
                    'desc': 'Under the cumulus at Woodside, BC, Canada'
                }
        },
        {           
            'weight': 3.5,
            'contenttype': 'video',
            'datas': 
                {
                    'provider': 'youtube',
                    'title': 'Flying at Chorges',
                    'desc': 'My last flight at Chorges',
                    'provider_id': '53MsjUi1F_E',
                },
        },
        {
            'weight': 4.3,
            'contenttype': 'flightlog',
            'datas':
                {
                    'pilot': Member.objects.all()[1],
                    'date':'2015-04-08T02:49:49.216456',
                    'take_off': 'Laffrey',
                    'landing': 'La guitare',
                    'track': [],
                    'gear': 
                        [
                            {
                                'gear_type': 'Parapente',
                                'name': 'Ozone Enzo 2'
                            }
                        ],
                }
        },
        {
            'weight': 4.3,
            'contenttype': 'flightlog',
            'datas':
                {
                    'pilot': Member.objects.all()[0],
                    'date':'2015-04-08T02:49:49.216456',
                    'take_off': 'Courtet',
                    'landing': 'Courtet',
                    'track': [],
                    'gear': 
                        [
                            {
                                'gear_type': 'Parapente',
                                'name': 'AirDesign Rise M'
                            }
                        ],
                }
        },
    ]
    
    form_prepare_next_trip = CreateTripForm()
    latest_users = Member.objects.all()[:5]
    context = {'latest_users': latest_users, 'news': news, 'form_prepare_next_trip': form_prepare_next_trip}
    return render(request, 'page/index.html', context)