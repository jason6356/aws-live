# S3 Service Developed by KS

- This is a service component developed to support uploading the S3 within the scope of using local development

- However the tests are still not yet completed yet due to the S3 manual is not running yet on actual EC2 instance

## Prerequisite needed

- **config.py** from the aws-live template configured with your settings
- **.env** environment file to store your aws credential to have access to the S3 Bucket
- **Learner Lab** has started in AWS console

### Setting up

#### Install python-dotenv

> pip install python-dotenv

1. Create a **.env** file in your root directory
2. Go to AWS Console, beside the End Lab, **i Aws Details**
3. Click the "Show" beside the **AWS CLI** : Show
4. It should show something like this
   ```env
   [default]
   aws_access_key_id=ASIASOMY2LJT2VGY2MEE
   aws_secret_access_key=VO71BZS7glPFDFc9NnFbffXvKNrC5yTbTTxmTYOt
   aws_session_token=asdlasldjlkajdjadd+14qSgeftiLPASEzI9Ey+hQIFttufVxTFD2XcW8CWnMAtk18sFrn3sz1kjd4btFcrQbpQiEgITF8Y4MbUJjOVRJwf/xreA3q3bCK4RmMy7Z0IKtL9mHGfEjApx0b+is63KQB5+CS68bLX3rhQZP7yrZxBbah2Y4YCylolY11mPyRfDzv3Ec4ucC6MphpsX2vjGVb3qzuhzSVWsvBkKHA7vmFjdRYjt4lxp/UfiSddOFtGaWov08Xr27E7YqvR7vVjriHn8cExhiPykukOthoBnM6DU70BM8NYSiex4qoBjItYICMwZdvAjcjIX/7HN0x9InLdkNX+98cAfMqkG4qblmVKb/FndNaA8B0SMVd
   ```
   Note : This credential is to illustrate how the access keys looks like
5. Copy and Paste this into the **.env** file
6. For sake of development, add a new attribute into **config.py**
   Add isEc2Instance and set it to False

```py

#customhost = "database-1.cgj7jfy75lmm.us-east-1.rds.amazonaws.com"
customhost = "internship-system.cgj7jfy75lmm.us-east-1.rds.amazonaws.com"
customuser = "aws_user"
custompass = "Bait3273"
#customdb = "employee"
customdb = "internship"
custombucket = "lohkangsheng-employee"
customregion = "us-east-1"
isEc2Instance = False

```

### Sample Code of Using the Service

```py

#Note s3_service is imported via folder, because i have multiple services
from services.s3_service import uploadToS3, getProgressionReports
#Yours can be
#from s3_service import uploadToS3,

@student_controller.route('/uploadProgress', methods=['POST'])
@require_session
def uploadProgressReport():
    file = request.files['file']
    #check file type is pdf
    if file.filename.split('.')[1] != 'pdf':
        status = "Error: File is not pdf"
        print(status)
        return status

    #Get the student id, and today's date, to generate the file
    student_id = session['student_id']
    now = datetime.now()
    ts = now.timestamp()

    path = f'students/{student_id}/progression_report_{ts}.pdf'

    uploadToS3(file, path)
    return "Success"

```

### Before Deployment

- Just Enable isEc2Instance to True before push to git for Ec2 to Clone
