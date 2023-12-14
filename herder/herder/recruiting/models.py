from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class CharacterClass(models.TextChoices):
    WARRIOR = 'WAR', 'Warrior'
    ROGUE = 'ROG', 'Rogue'
    CLERIC = 'CLR', 'Cleric'
    RANGER = 'RNG', 'Ranger'
    SHADOWKNIGHT = 'SHD', 'Shadow Knight'
    DRUID = 'DRU', 'Druid'
    MONK = 'MNK', 'Monk'
    BARD = 'BRD', 'Bard'
    PALADIN = 'PAL', 'Paladin'
    SHAMAN = 'SHM', 'Shaman'
    NECROMANCER = 'NEC', 'Necromancer'
    ENCHANTER = 'ENC', 'Enchanter'
    WIZARD = 'WIZ', 'Wizard'
    MAGICIAN = 'MAG', 'Magician'
    BERSERKER = 'BER', 'Berserker'


class ApplicationStatus(models.TextChoices):
    """Application status choices
    
    PENDING: Application has been submitted but not yet reviewed
    ACCEPTED: Application has been accepted by an officer
    REJECTED: Application has been rejected by an officer
    WITHDRAWN: Application has been withdrawn by the applicant
    """

    PENDING = 'P', 'Pending'
    APPROVED = 'A', 'Approved'
    REJECTED = 'R', 'Rejected'
    WITHDRAWN = 'W', 'Withdrawn'


class Application(models.Model):
    """Application model for recruiting

    The following are the questions asked in the current application form:

    1. These are the questions asked on the application form. The answers are stored in the ApplicationAnswer model.
    2. What is your character name, class, and level, & why would you like to join Kittens Who Say Meow?
    3. Do you know anyone in Kittens? 
    4. Have you grouped or spent quality time with any Kittens?
    5. What are your expectations of being a member of Kittens Who Say Meow, and what can Kittens Who Say Meow expect from you? 
    6. What sorts of characteristics will you bring (or hope to bring) to Kittens?
    7. Your group is in the Fireplace in Unrest, and another group moves to the hallway leading downstairs and starts pulling monsters over your group without saying anything. How do you react?
    8. Optional: What are the names and levels of your alts and would you like these characters invited to the guild as well?
    9. Additional comments you'd like to add 

    Attributes:
        user: The user who submitted the application
        status: The status of the application
        main_character: The name of the character the applicant wants to join the guild with
        class_name: The class of the character the applicant wants to join the guild with
        level: The level of the character the applicant wants to join the guild with
        reason: The applicant's reason for wanting to join the guild
        know_anyone: The applicant's answer to the question "Do you know anyone in Kittens?"
        grouped_with_anyone: The applicant's answer to the question "Have you grouped or spent quality time with any Kittens?"
        expectations: The applicant's answer to the question "What are your expectations of being a member of Kittens Who Say Meow, and what can Kittens Who Say Meow expect from you?"
        characteristics: The applicant's answer to the question "What sorts of characteristics will you bring (or hope to bring) to Kittens?"
        group_in_fireplace: The applicant's answer to the question "Your group is in the Fireplace in Unrest, and another group moves to the hallway leading downstairs and starts pulling monsters over your group without saying anything. How do you react?"
        alts: The applicant's answer to the question "What are the names and levels of your alts and would you like these characters invited to the guild as well?"
        comments: The applicant's answer to the question "Additional comments you'd like to add"
        created_at: The date and time the application was submitted
        updated_at: The date and time the application was last updated
    """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.PENDING,
    )

    main_character = models.CharField(
        max_length=64, 
        help_text="What is your character's name?"
        )
    
    class_name = models.CharField(
        max_length=3,
        choices=CharacterClass.choices,
        default=CharacterClass.WARRIOR,
    )

    level = models.IntegerField(
        default=15, 
        validators=[MinValueValidator(15), MaxValueValidator(60)],
        help_text="What is your character's level?"
        )
    
    reason = models.TextField(
        help_text="Why would you like to join Kittens Who Say Meow?"
        )
    
    know_anyone = models.TextField(
        help_text="Do you know anyone in Kittens?"
        )
    
    grouped_with_anyone = models.TextField(
        help_text="Have you grouped or spent quality time with any Kittens?"
        )
    
    expectations = models.TextField(
        help_text="What are your expectations of being a member of Kittens Who Say Meow, and what can Kittens Who Say Meow expect from you?"
        )
    
    characteristics = models.TextField(
        help_text="What sorts of characteristics will you bring (or hope to bring) to Kittens?")
    
    group_in_fireplace = models.TextField(
        help_text="Your group is in the Fireplace in Unrest, and another group moves to the hallway leading downstairs and starts pulling monsters over your group without saying anything. How do you react?"
        )
    
    alts = models.TextField(
        help_text="What are the names and levels of your alts and would you like these characters invited to the guild as well?"
        )

    comments = models.TextField(
        help_text="Additional comments you'd like to add"
        )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        """String representation of the Application model"""
        return self.main_character
    
    
    def approve(self) -> None:
        """Approve an application"""
        self.status = ApplicationStatus.APPROVED
        
    
    def reject(self) -> None:
        """Reject an application"""
        self.status = ApplicationStatus.REJECTED
        

    def withdraw(self) -> None:
        """Withdraw an application"""
        self.status = ApplicationStatus.WITHDRAWN
        
    
    class Meta:
        """Meta class for Application model"""
        ordering = ['-created_at']
        verbose_name_plural = 'applications'

