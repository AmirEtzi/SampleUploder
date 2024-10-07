from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    # images = forms.FileField(
    #     widget=forms.FileInput(
    #         attrs={
    #             "multiple": True,  # Allow multiple file uploads
    #             "class": "form-control",
    #             "style": "max-width: 300px; font-size: 12px;",
    #         }
    #     ),
    #     required=False,
    # )

    class Meta:
        model = Post
        fields = ("title", "category", "author", "body", "link")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; font-size: 12px;",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; font-size: 12px;",
                }
            ),
            "author": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; font-size: 12px;",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; height: 100px; font-size: 12px;",
                }
            ),
            "link": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; font-size: 12px;",
                }
            ),
        }


# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         fields = ("title", "author", "body", "link", "image")
#         widgets = {
#             "title": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "style": "max-width: 300px; font-size: 12px;",  # Adjust size here
#                 }
#             ),
#             "author": forms.Select(
#                 attrs={
#                     "class": "form-control",
#                     "style": "max-width: 300px; font-size: 12px;",
#                 }
#             ),
#             "body": forms.Textarea(
#                 attrs={
#                     "class": "form-control",
#                     "style": "max-width: 300px; height: 100px; font-size: 12px;",
#                 }
#             ),
#             "link": forms.URLInput(
#                 attrs={
#                     "class": "form-control",
#                     "style": "max-width: 300px; font-size: 12px;",
#                 }
#             ),
#             "image": forms.ClearableFileInput(
#                 attrs={
#                     "class": "form-control",
#                     "style": "max-width: 300px; font-size: 12px;",
#                 }
#             ),
#         }
