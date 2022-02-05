# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WpArmActivity(models.Model):
    arm_activity_id = models.AutoField(primary_key=True)
    arm_user_id = models.BigIntegerField()
    arm_type = models.CharField(max_length=50)
    arm_action = models.CharField(max_length=50)
    arm_content = models.TextField()
    arm_item_id = models.BigIntegerField()
    arm_paid_post_id = models.BigIntegerField()
    arm_link = models.CharField(max_length=255, blank=True, null=True)
    arm_ip_address = models.CharField(max_length=50)
    arm_date_recorded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_activity'


class WpArmAutoMessage(models.Model):
    arm_message_id = models.AutoField(primary_key=True)
    arm_message_type = models.CharField(max_length=50)
    arm_message_period_unit = models.IntegerField(blank=True, null=True)
    arm_message_period_type = models.CharField(max_length=50, blank=True, null=True)
    arm_message_subscription = models.CharField(max_length=255)
    arm_message_subject = models.TextField()
    arm_message_content = models.TextField()
    arm_message_status = models.IntegerField()
    arm_message_send_copy_to_admin = models.IntegerField()
    arm_message_send_diff_msg_to_admin = models.IntegerField()
    arm_message_admin_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_arm_auto_message'


class WpArmBadgesAchievements(models.Model):
    arm_badges_id = models.AutoField(primary_key=True)
    arm_badges_parent = models.IntegerField()
    arm_badges_name = models.CharField(max_length=255, blank=True, null=True)
    arm_badges_type = models.CharField(max_length=50, blank=True, null=True)
    arm_badges_icon = models.TextField(blank=True, null=True)
    arm_badges_achievement = models.TextField(blank=True, null=True)
    arm_badges_achievement_type = models.CharField(max_length=50, blank=True, null=True)
    arm_badges_tooltip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_arm_badges_achievements'


class WpArmCoupons(models.Model):
    arm_coupon_id = models.AutoField(primary_key=True)
    arm_coupon_code = models.CharField(max_length=255)
    arm_coupon_label = models.CharField(max_length=255, blank=True, null=True)
    arm_coupon_discount = models.FloatField()
    arm_coupon_discount_type = models.CharField(max_length=50)
    arm_coupon_period_type = models.CharField(max_length=50)
    arm_coupon_on_each_subscriptions = models.IntegerField(blank=True, null=True)
    arm_coupon_start_date = models.DateTimeField()
    arm_coupon_expire_date = models.DateTimeField()
    arm_coupon_subscription = models.TextField(blank=True, null=True)
    arm_coupon_allow_trial = models.IntegerField()
    arm_coupon_allowed_uses = models.IntegerField()
    arm_coupon_used = models.IntegerField()
    arm_coupon_status = models.IntegerField()
    arm_coupon_added_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_coupons'


class WpArmDripRules(models.Model):
    arm_rule_id = models.BigAutoField(primary_key=True)
    arm_item_id = models.PositiveBigIntegerField()
    arm_item_type = models.CharField(max_length=50, blank=True, null=True)
    arm_rule_type = models.CharField(max_length=50, blank=True, null=True)
    arm_show_old_items = models.IntegerField()
    arm_rule_options = models.TextField(blank=True, null=True)
    arm_rule_plans = models.TextField(blank=True, null=True)
    arm_rule_status = models.IntegerField()
    arm_created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_drip_rules'


class WpArmEmailTemplates(models.Model):
    arm_template_id = models.AutoField(primary_key=True)
    arm_template_name = models.CharField(max_length=255)
    arm_template_slug = models.CharField(max_length=255)
    arm_template_subject = models.CharField(max_length=255)
    arm_template_content = models.TextField()
    arm_template_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_arm_email_templates'


class WpArmEntries(models.Model):
    arm_entry_id = models.BigAutoField(primary_key=True)
    arm_entry_email = models.CharField(max_length=255, blank=True, null=True)
    arm_name = models.CharField(max_length=255, blank=True, null=True)
    arm_description = models.TextField(blank=True, null=True)
    arm_ip_address = models.TextField(blank=True, null=True)
    arm_browser_info = models.TextField(blank=True, null=True)
    arm_entry_value = models.TextField(blank=True, null=True)
    arm_form_id = models.IntegerField(blank=True, null=True)
    arm_user_id = models.BigIntegerField(blank=True, null=True)
    arm_plan_id = models.IntegerField(blank=True, null=True)
    arm_is_post_entry = models.IntegerField()
    arm_paid_post_id = models.BigIntegerField()
    arm_created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_entries'


class WpArmFailAttempts(models.Model):
    arm_fail_attempts_id = models.BigAutoField(primary_key=True)
    arm_user_id = models.BigIntegerField()
    arm_fail_attempts_detail = models.TextField(blank=True, null=True)
    arm_fail_attempts_ip = models.CharField(max_length=200, blank=True, null=True)
    arm_is_block = models.IntegerField()
    arm_fail_attempts_datetime = models.DateTimeField()
    arm_fail_attempts_release_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_fail_attempts'


class WpArmFormField(models.Model):
    arm_form_field_id = models.AutoField(primary_key=True)
    arm_form_field_form_id = models.IntegerField()
    arm_form_field_order = models.IntegerField()
    arm_form_field_slug = models.CharField(max_length=255, blank=True, null=True)
    arm_form_field_option = models.TextField(blank=True, null=True)
    arm_form_field_bp_field_id = models.IntegerField()
    arm_form_field_status = models.IntegerField()
    arm_form_field_created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_form_field'


class WpArmForms(models.Model):
    arm_form_id = models.AutoField(primary_key=True)
    arm_form_label = models.CharField(max_length=255, blank=True, null=True)
    arm_form_title = models.CharField(max_length=255, blank=True, null=True)
    arm_form_type = models.CharField(max_length=100, blank=True, null=True)
    arm_form_slug = models.CharField(max_length=255, blank=True, null=True)
    arm_is_default = models.IntegerField()
    arm_set_name = models.CharField(max_length=255, blank=True, null=True)
    arm_set_id = models.IntegerField()
    arm_is_template = models.IntegerField()
    arm_ref_template = models.IntegerField()
    arm_form_settings = models.TextField(blank=True, null=True)
    arm_form_updated_date = models.DateTimeField()
    arm_form_created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_forms'


class WpArmLockdown(models.Model):
    arm_lockdown_id = models.BigAutoField(db_column='arm_lockdown_ID', primary_key=True)  # Field name made lowercase.
    arm_user_id = models.BigIntegerField()
    arm_lockdown_date = models.DateTimeField()
    arm_release_date = models.DateTimeField()
    arm_lockdown_ip = models.CharField(db_column='arm_lockdown_IP', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_arm_lockdown'


class WpArmLoginHistory(models.Model):
    arm_history_id = models.AutoField(primary_key=True)
    arm_user_id = models.IntegerField()
    arm_logged_in_ip = models.CharField(max_length=255)
    arm_logged_in_date = models.DateTimeField()
    arm_logout_date = models.DateTimeField()
    arm_login_duration = models.TimeField()
    arm_history_browser = models.CharField(max_length=255)
    arm_history_session = models.CharField(max_length=255)
    arm_login_country = models.CharField(max_length=255)
    arm_user_current_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_arm_login_history'


class WpArmMemberTemplates(models.Model):
    arm_id = models.AutoField(primary_key=True)
    arm_title = models.TextField(blank=True, null=True)
    arm_slug = models.CharField(max_length=255, blank=True, null=True)
    arm_type = models.CharField(max_length=50, blank=True, null=True)
    arm_default = models.IntegerField()
    arm_subscription_plan = models.TextField(blank=True, null=True)
    arm_core = models.IntegerField()
    arm_template_html = models.TextField(blank=True, null=True)
    arm_ref_template = models.IntegerField()
    arm_options = models.TextField(blank=True, null=True)
    arm_html_before_fields = models.TextField(blank=True, null=True)
    arm_html_after_fields = models.TextField(blank=True, null=True)
    arm_enable_admin_profile = models.IntegerField()
    arm_created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_member_templates'


class WpArmMembers(models.Model):
    arm_member_id = models.BigAutoField(primary_key=True)
    arm_user_id = models.PositiveBigIntegerField()
    arm_user_login = models.CharField(max_length=60)
    arm_user_pass = models.CharField(max_length=64)
    arm_user_nicename = models.CharField(max_length=50)
    arm_user_email = models.CharField(max_length=100)
    arm_user_url = models.CharField(max_length=100)
    arm_user_registered = models.DateTimeField()
    arm_user_activation_key = models.CharField(max_length=60)
    arm_user_status = models.IntegerField()
    arm_display_name = models.CharField(max_length=250)
    arm_user_type = models.IntegerField()
    arm_primary_status = models.IntegerField()
    arm_secondary_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_arm_members'


class WpArmMembershipSetup(models.Model):
    arm_setup_id = models.AutoField(primary_key=True)
    arm_setup_name = models.CharField(max_length=255)
    arm_setup_type = models.IntegerField()
    arm_setup_modules = models.TextField(blank=True, null=True)
    arm_setup_labels = models.TextField(blank=True, null=True)
    arm_status = models.IntegerField()
    arm_created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_membership_setup'


class WpArmPaymentLog(models.Model):
    arm_log_id = models.AutoField(primary_key=True)
    arm_invoice_id = models.IntegerField()
    arm_user_id = models.BigIntegerField()
    arm_first_name = models.CharField(max_length=255, blank=True, null=True)
    arm_last_name = models.CharField(max_length=255, blank=True, null=True)
    arm_plan_id = models.BigIntegerField()
    arm_old_plan_id = models.BigIntegerField()
    arm_payment_gateway = models.CharField(max_length=50)
    arm_payment_type = models.CharField(max_length=50)
    arm_token = models.TextField(blank=True, null=True)
    arm_payer_email = models.CharField(max_length=255, blank=True, null=True)
    arm_receiver_email = models.CharField(max_length=255, blank=True, null=True)
    arm_transaction_id = models.TextField(blank=True, null=True)
    arm_transaction_payment_type = models.CharField(max_length=100, blank=True, null=True)
    arm_transaction_status = models.TextField(blank=True, null=True)
    arm_payment_date = models.DateTimeField()
    arm_payment_mode = models.CharField(max_length=255, blank=True, null=True)
    arm_payment_cycle = models.IntegerField()
    arm_bank_name = models.CharField(max_length=255, blank=True, null=True)
    arm_account_name = models.CharField(max_length=255, blank=True, null=True)
    arm_additional_info = models.TextField(blank=True, null=True)
    arm_payment_transfer_mode = models.CharField(max_length=255, blank=True, null=True)
    arm_amount = models.FloatField()
    arm_currency = models.CharField(max_length=50, blank=True, null=True)
    arm_extra_vars = models.TextField(blank=True, null=True)
    arm_response_text = models.TextField(blank=True, null=True)
    arm_coupon_code = models.CharField(max_length=255, blank=True, null=True)
    arm_coupon_discount = models.FloatField()
    arm_coupon_discount_type = models.CharField(max_length=50, blank=True, null=True)
    arm_coupon_on_each_subscriptions = models.IntegerField(blank=True, null=True)
    arm_is_post_payment = models.IntegerField()
    arm_paid_post_id = models.BigIntegerField()
    arm_is_trial = models.IntegerField()
    arm_display_log = models.IntegerField()
    arm_created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_payment_log'


class WpArmSubscriptionPlans(models.Model):
    arm_subscription_plan_id = models.AutoField(primary_key=True)
    arm_subscription_plan_name = models.CharField(max_length=255)
    arm_subscription_plan_description = models.TextField(blank=True, null=True)
    arm_subscription_plan_type = models.CharField(max_length=50)
    arm_subscription_plan_options = models.TextField(blank=True, null=True)
    arm_subscription_plan_amount = models.FloatField()
    arm_subscription_plan_status = models.IntegerField()
    arm_subscription_plan_role = models.CharField(max_length=100, blank=True, null=True)
    arm_subscription_plan_post_id = models.BigIntegerField()
    arm_subscription_plan_is_delete = models.IntegerField()
    arm_subscription_plan_created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_arm_subscription_plans'


class WpArmTermmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    arm_term_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_arm_termmeta'


class WpCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_commentmeta'


class WpComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.PositiveBigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_comments'


class WpLinks(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.PositiveBigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_links'


class WpOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_options'


class WpPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_postmeta'


class WpPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.PositiveBigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.PositiveBigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_posts'


class WpTermRelationships(models.Model):
    object_id = models.PositiveBigIntegerField(primary_key=True)
    term_taxonomy_id = models.PositiveBigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'),)


class WpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.PositiveBigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)


class WpTermmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_termmeta'


class WpTerms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_terms'


class WpUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_usermeta'


class WpUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'wp_users'
