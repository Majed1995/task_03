from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "my_list" : [
            {
            'restaurant_name' : 'Tatami',
            'food_type': 'Japanese',
        },
        {
            'restaurant_name' : 'Texas Roadhouse ',
            'food_type': 'American',
        },
        {
            'restaurant_name' : 'Elevation Burger ',
            'food_type': 'Burgers',
        },
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object" : 
        {
            "restaurant_name" : "Istanbul",
            "food_type" : "Turkish"
        }
    }
    return render(request, 'detail.html', context)
