from django import forms


class AudioRecorderWidget(forms.ClearableFileInput):
    template_name = "admin/audio_recorder_widget.html"

    class Media:
        js = ("js/audio_recorder.js",)
