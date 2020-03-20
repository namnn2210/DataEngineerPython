import boto3

######################## SNS #############################

# sns = boto3.client('sns')

# Create topic
# response = sns.create_topic(Name='topic-01-namngoc')
# topic_arn = response['TopicArn']

# Get list topics
#response = sns.list_topics()

# Delete topics
# sns.delete_topic(TopicArn)

# Subscribe
# response_sms = sns.subscribe(TopicArn='arn:aws:sns:us-east-2:261080444714:topic-01-namngoc', Protocol='SMS',Endpoint='+84832301997')
# response_email = sns.subscribe(TopicArn='arn:aws:sns:us-east-2:261080444714:topic-01-namngoc', Protocol='Email',Endpoint='vohophuongnam@gmail.com')

# List subscriptions
# subscriptions = sns.list_subscriptions_by_topic(TopicArn)
# subscriptions = sns.list_subscriptions()['Subscriptions']

# Unsubscribe
# response = sns.unsubscribe(SubscriptionArn)

# Publish a topic
# sns.publish(TopicArn='arn:aws:sns:us-east-2:261080444714:topic-01-namngoc', Message="Nam gay dien", Subject='Nam gay dien')

#################### REKOGNITION ####################

# rekognition = boto3.client('rekognition')

# Detect Object
# response = rekognition.detect_labels(
#     Image={
#         'S3Object': {
#             'Bucket': 'bucket-namngoc-01',
#             'Name': 'detect.png'
#         }
#     },
#     MaxLabels=10,
#     MinConfidence=95
# )

# Detect Text
# response = rekognition.detect_text(
#     Image={
#         'S3Object':{
#             'Bucket':'bucket-namngoc-01',
#             'Name':'detect.png'
#         }
#     }
# )
# print(response)

#################### COMPREHEND TEXT #####################

# Translate text
# client = boto3.client('translate')
# translate = client.translate_text(
#     Text='Hello',
#     SourceLanguageCode='auto',
#     TargetLanguageCode='es'
# )

# Comprehend text
client = boto3.client('comprehend')
comprehend = client.detect_dominal_language(
    Text='Hello'
)
sentiment = client.detect_sentiment(
    Text='Hello',
    LanguageCode='end')['Sentiment']
