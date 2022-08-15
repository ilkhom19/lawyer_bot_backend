from django.db.models.signals import post_save
from django.dispatch import receiver
from .parser import make_paired_sentences
from .models import Article, Answer


@receiver(post_save, sender=Article)
def post_save_article(created, **kwargs):
    instance = kwargs['instance']
    if not created:
        Answer.objects.filter(article=instance.pk).delete()

    paired_sentences = make_paired_sentences(instance.text)
    if len(paired_sentences) > 1:
        for pair in paired_sentences:
            answer = Answer.objects.create(
                campaign_id=instance.campaign_id,
                language_id=instance.language_id,
                text=pair,
                article_id=instance.pk
            )
            answer.save()
    else:
        answer = paired_sentences
        answer.save()