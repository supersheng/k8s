#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import absolute_import

import six

from .common import ObjectMeta
from ..base import Model
from ..fields import Field, ListField


class PodDisruptionBudgetMatchExpressions(Model):
    key = Field(six.text_type)
    operator = Field(six.text_type)
    values = ListField(six.text_type)


class PodDisruptionBudgetSelector(Model):
    matchExpressions = Field(PodDisruptionBudgetMatchExpressions)
    matchLabels = Field(dict)


class PodDisruptionBudgetSpec(Model):
    minAvailable = Field(six.text_type)
    maxUnavailable = Field(six.text_type)
    selector = Field(PodDisruptionBudgetSelector)


class PodDisruptionBudget(Model):
    class Meta:
        url_template = "/apis/autoscaling/v1/namespaces/{namespace}/poddisruptionbudget/{name}"

    metadata = Field(ObjectMeta)
    spec = Field(PodDisruptionBudgetSpec)
