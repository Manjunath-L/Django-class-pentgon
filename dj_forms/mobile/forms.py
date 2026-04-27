from django import forms


class MobileForm(forms.Form):
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    price = forms.IntegerField()
    ram = forms.IntegerField()
    rom = forms.IntegerField()
    battery = forms.IntegerField()

    # # field level validation
    #     def clean_battery(self):
    #         battery = self.cleaned_data["battery"]
    #         if battery < 3000:
    #             raise forms.ValidationError("Battery capacity must be at least 3000 mAh.")
    #         return battery

    #     def clean_ram(self):
    #         ram = self.cleaned_data["ram"]
    #         if ram < 4:
    #             raise forms.ValidationError("RAM must be at least 4 GB.")
    #         return ram

    # object level validation
    def clean(self):
        cleaned_data = super().clean()

        battery = cleaned_data["battery"]
        if battery < 3000:
            raise forms.ValidationError("Battery capacity must be at least 3000 mAh.")

        ram = cleaned_data["ram"]
        if ram < 4:
            raise forms.ValidationError("RAM must be at least 4 GB.")

        return cleaned_data
