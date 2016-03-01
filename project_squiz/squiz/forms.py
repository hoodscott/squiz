class QuestionForm(forms.ModelForm):
    
    # question and answer as text
    question = forms.CharField(max_length=128,
                                label = "Question",)
    answer = forms.CharField(max_length=128,
                                label = "Question",)
    
    # optional image
    image = forms.ImageField(label="Upload Image",
                            required=False,)# can be null
    
    # creator of the question
    creator = forms.IntegerField(widget = forms.HiddenInput(), required=False)
    
    class Meta:
        model = Question
        fields = ('question', 'answer', 'image', 'creator')
        exclude = []
        
class RoundForm(forms.ModelForm):
    
    # question and answer as text
    name = forms.CharField(max_length=128,
                                label = "Round Name",)
    
    # creator of the question
    creator = forms.IntegerField(widget = forms.HiddenInput(), required=False)
    
    class Meta:
        model = Round
        fields = ('name', 'creator')
        exclude = []
        
class QuizForm(forms.ModelForm):
    
    # question and answer as text
    name = forms.CharField(max_length=128,
                                label = "Quiz Name",)
    
    # creator of the question
    creator = forms.IntegerField(widget = forms.HiddenInput(), required=False)
    
    class Meta:
        model = Quiz
        fields = ('name', 'creator')
        exclude = []
    
