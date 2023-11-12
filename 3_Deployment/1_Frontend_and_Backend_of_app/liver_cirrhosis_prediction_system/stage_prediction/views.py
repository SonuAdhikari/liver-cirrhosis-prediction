from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from stage_prediction.models import Input, InputForm, Output

def stage_prediction(request):

    if request.method == 'POST':
        user_input = InputForm(request.POST)
        if user_input.is_valid():

            # Save the user input values into input table
            user_input.save()

            # Read the input1 and input2 from the input table
            last_row_input = Input.objects.last()
            input_form = InputForm(initial=last_row_input.__dict__)

            # Calculate the total_number
            input1 = last_row_input.input1
            input2 = last_row_input.input2
            total_number = input1 + input2
            
            # Save the output1 value in the table
            Output(output1 = total_number).save()

            # Read the output1 from the output table
            output_last_recorded = Output.objects.last()
            output = output_last_recorded.output1


            return render(request, 'index.html', {'input_form': input_form,
                                                  'output': output})

    else:
        input_form = InputForm()
        return render(request, 'index.html', {'input_form': input_form})