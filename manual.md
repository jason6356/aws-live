# S3 Service Developed by KS

- This is a service component developed to support uploading the S3 within the scope of using local development

- However the tests are still not yet completed yet due to the S3 manual is not running yet on actual EC2 instance

## Prerequisite needed

- **config.py** from the aws-live template configured with your settings
- **.env** environment file to store your aws credential to have access to the S3 Bucket
- **Learner Lab** has started in AWS console

### Setting up

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
6. And you are done!

### Potential Risk that will be facing

- This service is not yet tested with deployment with EC2, actually
