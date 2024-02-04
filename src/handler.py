""" Example handler file. """

from transformers import pipeline
import runpod

pipe = pipeline("text2text-generation", model="google/flan-t5-small")

# If your handler runs inference on a model, load the model here.
# You will want models to be loaded into memory before starting serverless.


def handler(job):
    """ Handler function that will be used to process jobs. """
    job_input = job['input']
    message = job_input.get('message', 'Hi!')
    return pipe(message)


runpod.serverless.start({"handler": handler})
