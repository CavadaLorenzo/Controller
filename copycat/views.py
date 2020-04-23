from django.shortcuts import render
import requests, traceback
from .forms import TransferRequestForm
from .models import Transfer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import simplejson as json


@login_required
def copycat(request):
    """
    This method will create the form for a new TransferRequest. 
    This method can be accessible only from an authenticated user.

    :param request: the request received.

    If the request.method is POST the form is validated and, ii it is correct
    the time_span and view_count value will be extracted and a get request to the
    copycat API will be done. 
    The response of this request is than used to create a list of the performed transfer.

    :return: a render of the copycat page.
    """
    try:
        if request.method == 'POST':
            form = TransferRequestForm(request.POST)
            if form.is_valid():
                form.save()

                time = form.cleaned_data["time_span"]
                count = form.cleaned_data["view_count"]

                IP_COPYCAT = "http://192.168.1.188:4025?COUNT=count_value&TIME=time_span"
                IP_COPYCAT = IP_COPYCAT.replace("count_value", str(count))
                IP_COPYCAT = IP_COPYCAT.replace("time_span", str(time))

                response = requests.get(IP_COPYCAT).json()
                transfer_list = response['transfer']
                context = {'transfer_list': transfer_list,
                            'form': form}
                for transfer in context['transfer_list']:
                    t = Transfer()
                    t.filename = transfer['filename']
                    t.time = transfer['time']
                    t.from_server = transfer['from_server']
                    t.to_server = transfer['to_server']
                    t.save()
                
                messages.success(request, f'Success! Transfer Completed')
                return render(request, 'copycat/copycat.html', context)
        else:
            form = TransferRequestForm()
        return render(request, 'copycat/copycat.html', {'form': form})

    except requests.exceptions.ConnectionError:
        messages.warning(request, f'Attention! Copycat service has close the connection. Maybe is down or got an error?')
        return render(request, 'copycat/copycat.html', {'form': form})
    except json.decoder.JSONDecodeError:
        messages.warning(request, f'Attention! Copycat service hasn\'t returned a JSON object.')
        return render(request, 'copycat/copycat.html', {'form': form})
    except Exception:
        tb = traceback.format_exc()
        print(tb)
        messages.warning(request, f'Attention! An exception occured, for more information look at the terminal.')
        return render(request, 'copycat/copycat.html', {'form': form})
        