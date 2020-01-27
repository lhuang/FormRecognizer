using System;
namespace Amerigas.FormRecognizer
{
    public static class Constants
    {
        public static readonly string ServiceEndpoint = "https://formrecognizer-capture.cognitiveservices.azure.com/";
        public static readonly string SubscriptionKey = "89ea53ef01c248b2a1c27db02afb4527";
        public static readonly string TrainingDataUrl = "https://captureformsstore.blob.core.windows.net/forms?st=2020-01-25T09%3A14%3A20Z&se=2020-07-26T09%3A14%3A00Z&sp=racwdl&sv=2018-03-28&sr=c&sig=Lt2esZAJV5smvgtMSzyPHGGLctUI7ds8TppWOL3zFmE%3D";
        public static readonly string TestFile = "/~Dev/FormRecognizer-Python/SSO2.pdf";
    }
}
