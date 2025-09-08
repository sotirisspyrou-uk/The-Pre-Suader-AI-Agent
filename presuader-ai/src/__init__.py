"""
Pre-Suader AI Agent - Core Package
Version: 08-09-2025 17:40:00
Author: Sotiris Spyrou, CEO, VerityAI

Ethical Pre-Suasion Marketing Optimization
"""

__version__ = "1.0.0"
__author__ = "Sotiris Spyrou, CEO, VerityAI"
__description__ = "Ethical AI agent for pre-suasion marketing optimization"

from .presuader_core_functions import PreSuaderCore, AudienceProfile, PreSuasiveStrategy
from .metrics_tracker import MetricsTracker, CampaignPerformance

__all__ = [
    "PreSuaderCore",
    "AudienceProfile", 
    "PreSuasiveStrategy",
    "MetricsTracker",
    "CampaignPerformance"
]
