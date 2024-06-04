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
            rx.heading(
                "JHOSEPH CACERES ARAMAYO",
                class_name="font-extrabold text-2xl",
            ),
            rx.heading("Develop Frontend", class_name="text-xl font-medium"),
            rx.flex(
                rx.image(src="jose.jpg", class_name="w-[400px]"),
                rx.flex(
                    rx.heading("SKILLS", class_name="text-xl font-semibold"),
                    rx.list.unordered(
                        rx.list.item("TypeScript"),
                        rx.list.item("JavaScript"),
                        rx.list.item("Python"),
                        rx.list.item("Java"),
                        rx.list.item("Postgres"),
                        rx.list.item("Mysql"),
                        rx.list.item("Goland"),
                    ),
                    class_name="flex flex-col",
                ),
                class_name="gap-4 items-center",
            ),
            rx.text(
                "My passion for technology drives me to constantly explore new solutions and stay up to date with the latest advances. I excel at problem solving and find satisfaction in finding innovative solutions. My focus on continuous learning allows me to adapt quickly to changes and constantly improve my skills. I am committed to contributing to the field of computing with creativity and dedication.",
                class_name="text-lg",
            ),
            rx.heading("SKILLS", class_name="text-xl font-semibold"),
            rx.flex(
                rx.link(
                    rx.button("Facebook"),
                    href="https://www.facebook.com/jhoseph.caceresaramayo/",
                    is_external=True,
                ),
                rx.link(
                    rx.button("Instagram"),
                    href="https://www.instagram.com/jhoseph_caceres19/",
                    is_external=True,
                    class_name="bg-blue-600",
                ),
                rx.link(
                    rx.button("Linkedin"),
                    href="https://www.linkedin.com/in/jos%C3%A9-caceres-aramayo-9b7548268/",
                    is_external=True,
                ),
                class_name=" gap-4",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
