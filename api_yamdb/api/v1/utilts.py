"""Инструменты."""

from django.shortcuts import get_object_or_404
from reviews.models import Title


class CurrentTitleDefault:
    """Текущее произведение."""

    requires_context = True

    def __call__(self, serializer_field):
        """Получение произведения."""
        title_id = serializer_field.context['view'].kwargs.get('title_id')
        return get_object_or_404(Title, id=title_id)

    def __repr__(self):
        """Описание."""
        return '%s()' % self.__class__.__name__
