from django.shortcuts import render, redirect
from authentications.models import User
from .models import Patient_data
import pickle
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
# Create your views here.


def account(request):
    try:
        if request.session['email']:
            user = User
            query = User.objects.get(email=request.session['email'])
            name = query.name
            context = {'name': name}
            if request.session['type'] == 'patient':
                if request.method == 'POST':
                    gender = int(request.POST.get('gender'))
                    age = int(request.POST.get('age'))
                    smoking = int(request.POST.get('smoking'))
                    yellow_fingers = int(request.POST.get('yellow-fingers'))
                    anxiety = int(request.POST.get('anxiety'))
                    peer_pressure = int(request.POST.get('peer-pressure'))
                    chronic_disease = int(request.POST.get('chronic-disease'))
                    fatigue = int(request.POST.get('fatigue'))
                    allergy = int(request.POST.get('allergy'))
                    wheezing = int(request.POST.get('wheezing'))
                    alcohol_consumption = int(request.POST.get('alcohol-consumption'))
                    coughing = int(request.POST.get('coughing'))
                    short_breath = int(request.POST.get('short-breath'))
                    swallowing_difficulty = int(request.POST.get('swallowing-difficulty'))
                    chest_pain = int(request.POST.get('chest-pain'))
                    pred_arr = [[gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, \
                                 wheezing, alcohol_consumption, coughing, short_breath]]

                    model = pickle.load(open('static/model.pkl', 'rb'))
                    prediction = model.predict(pred_arr)

                    if prediction[0] == 1:
                        context['result'] = "POSITIVE"
                        dict1 = {1:"yes", 2:"no"}
                        dict2 = {1:"M", 2:'F'}
                        new_data = Patient_data.objects.create(patient= query, age=age, gender=dict2[gender], smoking=dict1[smoking], yellow_fingers=dict1[yellow_fingers], \
                                                               anxiety= dict1[anxiety], peer_pressure=dict1[peer_pressure], chronic_disease=dict1[chronic_disease], fatigue=dict1[fatigue], \
                                                               allergy=dict1[allergy], wheezing=dict1[wheezing], alcohol=dict1[alcohol_consumption], coughing=dict1[coughing],\
                                                               short_breath=dict1[short_breath], swallowing_difficulty=dict1[swallowing_difficulty], chest_pain=dict1[chest_pain])
                    else:
                        context['result'] = 'NEGATIVE'

                return render(request, 'account.html', context)
            else:

                if request.method == 'POST':
                    from tensorflow import keras
                    from tensorflow.keras.preprocessing import image
                    import numpy as np
                    from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
                    model = keras.models.load_model('static/mymodelVGG19_small.h5')
                    file = request.FILES.get('image')
                    id = request.POST.get('id')
                    print(file)
                    add_image_query = Patient_data.objects.get(id=id)
                    add_image_query.image = file
                    add_image_query.save()
                    image_name = str(add_image_query.image.url).split("/")

                    img_path = "media/lungs/" + str(image_name[-1])
                    img = image.load_img(img_path, target_size=(128, 128))
                    img_array = image.img_to_array(img)
                    img_batch = np.expand_dims(img_array, axis=0)
                    img_preprocessed = preprocess_input(img_batch)
                    prediction = model.predict(img_preprocessed)
                    print(prediction)
                    pred = np.argmax(model.predict(img_preprocessed), axis=-1)
                    if pred[0] == 0:
                        add_image_query.prediction = "LUNG ACA"
                    elif pred[0] == 1:
                        add_image_query.prediction = "LUNG N"
                    else:
                        add_image_query.prediction = "LUNG SCC"
                    add_image_query.save()

                query_patients = Patient_data.objects.all()
                context['patients'] = query_patients
                context['patients'] = query_patients
                return render(request, 'account2.html', context)
    except Exception as e:
        print(e)
        return redirect('login')