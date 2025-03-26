map_translations = {
    "des_hu_cm": "World's Edge",
    "tropic_mu2_cm": "Storm Point",
    "district_cm": "E-District",
    "moon_cm": "Broken Moon",
    "tdm_fragment_s_pm": "Fragment East",
    "mp_rr_thunderdome": "Thunderdome",
    

}

ability_translations = {
    "": "",
    "": ""
}

weapon_translations = {
    "": "",
    "": ""
}

class LiveApexTranslator():
    """
    # Translator

    This class contains functions to translate data.
    """

    def translateAbility(ability: str):
        """
        # Translate an Ability

        This function translates an ability from internal reference to in game reference.
        Basically converts the ability into a more understandable name.

        ## Parameters

        :ability: The ability to translate.

        ## Returns

        The translated ability name.

        ## Example

        ```python
        translateAbility('')
        ```

        ## Raises
        
        Exception: If the ability is unknown.
        """

        if ability in ability_translations:
            translated = ability_translations[ability]
        else:
            raise Exception(f"Unknown ability: {ability}")

        return translated
    
    def translateWeapon(weapon: str):
        """
        # Translate a Weapon

        This function translates a weapon from internal reference to in game reference.
        Basically converts the weapon into a more understandable name.

        ## Parameters

        :weapon: The weapon to translate.

        ## Returns

        The translated weapon name.

        ## Example

        ```python
        translateWeapon('')
        ```

        ## Raises

        Exception: If the weapon is unknown.
        """

        if weapon in weapon_translations:
            translated = weapon_translations[weapon]
        else:
            raise Exception(f"Unknown weapon: {weapon}")

        return translated