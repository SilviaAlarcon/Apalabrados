from django.shortcuts import render
import re
from django.db.models import Sum

#Models
from games.models import Alphanumeric, Number, Special_char, historical

def start_game(request):
    if request.method == 'POST':
        data = request.POST['data']

        import re
        special_char = re.findall(r'[\W_]', data)

        if len(special_char) > 0:
            convert_string = ''.join(special_char)
            special_charac = Special_char.objects.create(special_character=convert_string)
            special_charac.save()
        elif data.isdigit():
            accumulated_sum = Number.objects.all().aggregate(Sum('number'))
            accumulated_value = accumulated_sum['number__sum'] + int(data)
            number = Number.objects.create(number=data, accumulated=accumulated_value)
            number.save()
        else:
            initial = "".join([word[0] for word in data.split()])
            final = "".join([word[-1] for word in data.split()])
            alpha = Alphanumeric.objects.create(text=data, initial_letter=initial, final_letter=final)
            alpha.save()      

    return render(request, 'home.html')


def list_alphanumeric(request):
    alphanumeric = Alphanumeric.objects.all()
    context = {'alphanumeric': alphanumeric}
    return render(request, 'table_alphanumeric.html', context)


def list_number(request):
    number = Number.objects.all()
    context = {'number': number}
    return render(request, 'table_number.html', context)


def list_special_char(request):
    special_char = Special_char.objects.all()
    context = {'special_char': special_char}
    return render(request, 'table_special_char.html', context)
