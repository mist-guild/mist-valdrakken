from . import db


class ReagentCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.Text, nullable=False)
    boe_epic = db.Column(db.Integer, nullable=False)
    boe_rare = db.Column(db.Integer, nullable=False)
    boe_uncommon = db.Column(db.Integer, nullable=False)
    abrasive_polishing_cloth_bronze = db.Column(db.Integer, nullable=False)
    writhebark_bronze = db.Column(db.Integer, nullable=False)
    saxifrage_bronze = db.Column(db.Integer, nullable=False)
    shimmering_pigment_bronze = db.Column(db.Integer, nullable=False)
    spool_of_wilderthread_bronze = db.Column(db.Integer, nullable=False)
    hochenblume_bronze = db.Column(db.Integer, nullable=False)
    bubble_poppy_bronze = db.Column(db.Integer, nullable=False)
    aerated_mana_potion_bronze = db.Column(db.Integer, nullable=False)
    refreshing_healing_potion_bronze = db.Column(db.Integer, nullable=False)
    potion_of_gusts_bronze = db.Column(db.Integer, nullable=False)
    potion_of_the_hushed_zephyr_bronze = db.Column(db.Integer, nullable=False)
    adamant_scales_bronze = db.Column(db.Integer, nullable=False)
    resilient_leather_bronze = db.Column(db.Integer, nullable=False)
    lustrous_scaled_hide_bronze = db.Column(db.Integer, nullable=False)
    dense_hide_bronze = db.Column(db.Integer, nullable=False)
    potion_of_frozen_focus_bronze = db.Column(db.Integer, nullable=False)
    saxifrage_silver = db.Column(db.Integer, nullable=False)
    writhebark_silver = db.Column(db.Integer, nullable=False)
    hochenblume_silver = db.Column(db.Integer, nullable=False)
    lustrous_scaled_hide_silver = db.Column(db.Integer, nullable=False)
    dense_hide_silver = db.Column(db.Integer, nullable=False)
    resilient_leather_silver = db.Column(db.Integer, nullable=False)
    adamant_scales_silver = db.Column(db.Integer, nullable=False)
    hochenblume_gold = db.Column(db.Integer, nullable=False)
    resilient_leather_gold = db.Column(db.Integer, nullable=False)
    adamant_scales_gold = db.Column(db.Integer, nullable=False)
    awakened_air = db.Column(db.Integer, nullable=False)
    awakened_frost = db.Column(db.Integer, nullable=False)
    awakened_earth = db.Column(db.Integer, nullable=False)
    awakened_fire = db.Column(db.Integer, nullable=False)
    rousing_ire = db.Column(db.Integer, nullable=False)
    rousing_order = db.Column(db.Integer, nullable=False)
    rousing_decay = db.Column(db.Integer, nullable=False)
    rousing_fire = db.Column(db.Integer, nullable=False)
    rousing_air = db.Column(db.Integer, nullable=False)
    rousing_earth = db.Column(db.Integer, nullable=False)
    rousing_frost = db.Column(db.Integer, nullable=False)
    wildercloth = db.Column(db.Integer, nullable=False)
    tattered_wildercloth = db.Column(db.Integer, nullable=False)
    salamanther_scales = db.Column(db.Integer, nullable=False)
    flawless_proto_dragon_scale = db.Column(db.Integer, nullable=False)
    trailblazers_scale_bracers = db.Column(db.Integer, nullable=False)
    cacophonous_thunderscale = db.Column(db.Integer, nullable=False)
    chromatic_dust = db.Column(db.Integer, nullable=False)
    vibrant_shard = db.Column(db.Integer, nullable=False)
    resonant_crystal = db.Column(db.Integer, nullable=False)
    rockfang_leather = db.Column(db.Integer, nullable=False)
    fire_infused_hide = db.Column(db.Integer, nullable=False)
    elemental_mote = db.Column(db.Integer, nullable=False)
    mastodon_tusk = db.Column(db.Integer, nullable=False)
    woolly_mountain_pelt = db.Column(db.Integer, nullable=False)
    exceptional_pelt = db.Column(db.Integer, nullable=False)
    stonewatchers_thumb = db.Column(db.Integer, nullable=False)
    mighty_mammoth_ribs = db.Column(db.Integer, nullable=False)
    basilisk_eggs = db.Column(db.Integer, nullable=False)
    burly_bear_haunch = db.Column(db.Integer, nullable=False)
    uestionable_meat = db.Column(db.Integer, nullable=False)
    stonewatchers_eye = db.Column(db.Integer, nullable=False)
    hornswog_hunk = db.Column(db.Integer, nullable=False)
    windsong_plumage = db.Column(db.Integer, nullable=False)
    maybe_meat = db.Column(db.Integer, nullable=False)
    aquatic_maw = db.Column(db.Integer, nullable=False)
    stonewatchers_toe = db.Column(db.Integer, nullable=False)
    lava_beetle = db.Column(db.Integer, nullable=False)
    contoured_fowlfeather = db.Column(db.Integer, nullable=False)
    iridescent_plume = db.Column(db.Integer, nullable=False)
    tuskarr_jerky = db.Column(db.Integer, nullable=False)
    waterfowl_filet = db.Column(db.Integer, nullable=False)
    fluorescent_fluid = db.Column(db.Integer, nullable=False)
    primal_bear_spine = db.Column(db.Integer, nullable=False)
    bruffalon_flank = db.Column(db.Integer, nullable=False)
    tuft_of_primal_wool = db.Column(db.Integer, nullable=False)
    rich_illusion_dust = db.Column(db.Integer, nullable=False)
    pristine_vorquin_horn = db.Column(db.Integer, nullable=False)
    tallstrider_sinew = db.Column(db.Integer, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __str__(self) -> str:
        return self.character_name + ": " + self.id

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
