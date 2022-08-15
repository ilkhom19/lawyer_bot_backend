import tensorflow as tf
import tensorflow_hub as hub
# import numpy as np
import tensorflow_text
from django.db import models

from .apps import ApiConfig

class Answer(models.Model):
    text = models.TextField()

    def get_embedding(self):
        answer_context = self.text.split('. ', 1)
        answer = answer_context[0]
        if len(answer_context) > 1:
            context = answer_context[1]
        else:
            context = answer_context[0]

        embeddings = ApiConfig.neural_model.signatures['response_encoder'](
            input=tf.constant([answer, ]),
            context=tf.constant([context, ]))
        return list(embeddings['outputs'].numpy()[0])

    def __str__(self):
        return self.text