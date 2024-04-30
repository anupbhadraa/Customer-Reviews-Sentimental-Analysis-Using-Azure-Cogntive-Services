# Before running this file install the azure cognitive services -> text analysis library in the work enviroment

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

def analyze_sentiment(text):
    try:
        subscription_key = "3998ee3aa0b24baba6a6b520b1a3f61a"
        endpoint = "https://customerreview.cognitiveservices.azure.com/"

        credentials = CognitiveServicesCredentials(subscription_key)
        text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)

        response = text_analytics_client.sentiment(documents=[{"id": "1", "text": text}])

        sentiment_score = response.documents[0].score
        return sentiment_score
    except Exception as e:
        print("Encountered exception: {}".format(e))
        return None


def get_sentiment_label(score):
    if score >= 0.6:
        return "Positive"
    elif score >= 0.4:
        return "Neutral"
    else:
        return "Negative"


def main():
    print("Welcome to the Customer Feedback Sentiment Analysis Program!")

    while True:
        feedback = input("Enter your customer feedback (or type 'exit' to quit): ").strip()

        if feedback.lower() == 'exit':
            print("Exiting the program. Thank you!")
            break

        if not feedback:
            print("Feedback cannot be empty. Please provide valid feedback.")
            continue

        sentiment_score = analyze_sentiment(feedback)
        if sentiment_score is not None:
            sentiment_label = get_sentiment_label(sentiment_score)
            print("\nSentiment Analysis Results:")
            print("Feedback:", feedback)
            print("Sentiment Score:", sentiment_score)
            print("Sentiment Label:", sentiment_label)
            print("\n")

if __name__ == "__main__":
    main()