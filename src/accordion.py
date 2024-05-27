import dash_mantine_components as dmc
from dash import html

characters_list = [
    {
        "id": "bender",
        "image": "https://img.icons8.com/clouds/256/000000/futurama-bender.png",
        "label": "Intro",
        "description": "Fascinated with cooking, though has no sense of taste",
        "content": "Bender Bending Rodríguez, (born September 4, 2996), designated Bending Unit 22, and commonly "
        "known as Bender, is a bending unit created by a division of MomCorp in Tijuana, Mexico, "
        "and his serial number is 2716057. His mugshot id number is 01473. He is Fry's best friend.",
    },
    {
        "id": "carol",
        "image": "https://img.icons8.com/clouds/256/000000/futurama-mom.png",
        "label": "Em busca de um perfil",
        "description": "One of the richest people on Earth",
        "content": "Carol Miller (born January 30, 2880), better known as Mom, is the evil chief executive officer "
        "and shareholder of 99.7% of Momcorp, one of the largest industrial conglomerates in the universe "
        "and the source of most of Earth's robots. She is also one of the main antagonists of the Futurama "
        "series.",
    },
    {
        "id": "homer",
        "image": "https://img.icons8.com/clouds/256/000000/homer-simpson.png",
        "label": "Mas onde é que entra linguagens de programação?",
        "description": "Overweight, lazy, and often ignorant",
        "content": "Homer Jay Simpson (born May 12) is the main protagonist and one of the five main characters of "
        "The Simpsons series(or show). He is the spouse of Marge Simpson and father of Bart, "
        "Lisa and Maggie Simpson.",
    },
    {
        "id": "homer",
        "image": "https://img.icons8.com/clouds/256/000000/homer-simpson.png",
        "label": "Por que Python?",
        "description": "Overweight, lazy, and often ignorant",
        "content": "Homer Jay Simpson (born May 12) is the main protagonist and one of the five main characters of "
        "The Simpsons series(or show). He is the spouse of Marge Simpson and father of Bart, "
        "Lisa and Maggie Simpson.",
    },
    {
        "id": "homer",
        "image": "https://img.icons8.com/clouds/256/000000/homer-simpson.png",
        "label": "Primeiros passos",
        "description": "Overweight, lazy, and often ignorant",
        "content": "Homer Jay Simpson (born May 12) is the main protagonist and one of the five main characters of "
        "The Simpsons series(or show). He is the spouse of Marge Simpson and father of Bart, "
        "Lisa and Maggie Simpson.",
    },
    {
        "id": "homer",
        "image": "https://img.icons8.com/clouds/256/000000/homer-simpson.png",
        "label": "Mas onde é que entra linguagens de programação?",
        "description": "Overweight, lazy, and often ignorant",
        "content": "Homer Jay Simpson (born May 12) is the main protagonist and one of the five main characters of "
        "The Simpsons series(or show). He is the spouse of Marge Simpson and father of Bart, "
        "Lisa and Maggie Simpson.",
    },
]


def create_accordion_label(label, image, description):
    return dmc.AccordionControl(
        dmc.Group(
            [
                dmc.Avatar(src=image, radius="xl", size="xl", style={"zoom": "250%"}),
                html.Div(
                    [
                        dmc.Title(label, order=2),
                        dmc.Text(
                            description, 
                            size="xl", 
                            fw=400, 
                            c="dimmed", 
                            style={"zoom": "120%"}
                        ),
                    ]
                ),
            ]
        )
    )


def create_accordion_content(content):
    return dmc.AccordionPanel(dmc.Text(content, size="xl"))


accordion_comp = dmc.Accordion(
    chevronPosition="right",
    variant="contained",
    children=[
        dmc.AccordionItem(
            [
                create_accordion_label(
                    character["label"], character["image"], character["description"]
                ),
                create_accordion_content(character["content"]),
            ],
            value=character["id"],
        )
        for character in characters_list
    ],
)