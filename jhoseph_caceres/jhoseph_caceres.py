"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("JHOSEPH CACERES ARAMAYO", size="9"),
            
            rx.text(
                "My passion for technology drives me to constantly explore new solutions and stay up to date with the latest advances. I excel at problem solving and find satisfaction in finding innovative solutions. My focus on continuous learning allows me to adapt quickly to changes and constantly improve my skills. I am committed to contributing to the field of computing with creativity and dedication.",
                size="5",
            ),
            rx.link(
                rx.button("Facebook"),
                href="https://www.facebook.com/jhoseph.caceresaramayo/",
                is_external=True,
            ),
            rx.link(
                rx.button("Instagram"),
                href="https://www.instagram.com/jhoseph_caceres19/",
                is_external=True,
            ),
            rx.link(
                rx.button("Linkedin"),
                href="https://www.linkedin.com/in/jos%C3%A9-caceres-aramayo-9b7548268/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        
    )


app = rx.App()
app.add_page(index)
