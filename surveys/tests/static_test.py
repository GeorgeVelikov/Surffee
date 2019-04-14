from ..models.survey import Survey


# A helper function to create a new survey
def create_survey(name, creator, active=True, commit=True):
    survey = Survey(
        name=name,
        creator=creator,
        active=active)
    if commit:
        survey.save()
    return survey
