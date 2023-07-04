from customtkinter import CTkButton, CTkLabel

colors = {
    "slate-50": "#f8fafc",
    "slate-100": "#f1f5f9",
    "slate-200": "#e2e8f0",
    "slate-300": "#cbd5e1",
    "slate-400": "#94a3b8",
    "slate-500": "#64748b",
    "slate-600": "#475569",
    "slate-700": "#334155",
    "slate-800": "#1e293b",
    "slate-900": "#0f172a",
    "zinc-50": "#fafafa",
    "zinc-100": "#f5f5f5",
    "zinc-200": "#e5e5e5",
    "zinc-300": "#d4d4d4",
    "zinc-400": "#a3a3a3",
    "zinc-500": "#737373",
    "zinc-600": "#525252",
    "zinc-700": "#404040",
    "zinc-800": "#262626",
    "zinc-900": "#171717",
    "neutral-50": "#fafafa",
    "neutral-100": "#f4f4f5",
    "neutral-200": "#e5e5e5",
    "neutral-300": "#d4d4d4",
    "neutral-400": "#a3a3a3",
    "neutral-500": "#737373",
    "neutral-600": "#525252",
    "neutral-700": "#404040",
    "neutral-800": "#262626",
    "neutral-900": "#171717",
    "neutral-950": "#0a0a0a",
    "gray-50": "#f9fafb",
    "gray-100": "#f3f4f6",
    "gray-200": "#e5e7eb",
    "gray-300": "#d1d5db",
    "gray-400": "#9ca3af",
    "gray-500": "#6b7280",
    "gray-600": "#4b5563",
    "gray-700": "#374151",
    "gray-800": "#1f2937",
    "gray-900": "#111827",
    "red-50": "#fef2f2",
    "red-100": "#fee2e2",
    "red-200": "#fecaca",
    "red-300": "#fca5a5",
    "red-400": "#f87171",
    "red-500": "#ef4444",
    "red-600": "#dc2626",
    "red-700": "#b91c1c",
    "red-800": "#991b1b",
    "red-900": "#7f1d1d",
    "orange-50": "#fff7ed",
    "orange-100": "#ffedd5",
    "orange-200": "#fed7aa",
    "orange-300": "#fdba74",
    "orange-400": "#fb923c",
    "orange-500": "#f97316",
    "orange-600": "#ea580c",
    "orange-700": "#c2410c",
    "orange-800": "#9a3412",
    "orange-900": "#7c2d12",
    "amber-50": "#fffbeb",
    "amber-100": "#fef3c7",
    "amber-200": "#fde68a",
    "amber-300": "#fcd34d",
    "amber-400": "#fbbf24",
    "amber-500": "#f59e0b",
    "amber-600": "#d97706",
    "amber-700": "#b45309",
    "amber-800": "#92400e",
    "amber-900": "#78350f",
    "yellow-50": "#fefce8",
    "yellow-100": "#fef9c3",
    "yellow-200": "#fef08a",
    "yellow-300": "#fde047",
    "yellow-400": "#facc15",
    "yellow-500": "#eab308",
    "yellow-600": "#ca8a04",
    "yellow-700": "#a16207",
    "yellow-800": "#854d0e",
    "yellow-900": "#713f12",
    "green-50": "#f0fdf4",
    "green-100": "#dcfce7",
    "green-200": "#bbf7d0",
    "green-300": "#86efac",
    "green-400": "#4ade80",
    "green-500": "#22c55e",
    "green-600": "#16a34a",
    "green-700": "#15803d",
    "green-800": "#166534",
    "green-900": "#14532d",
    "teal-50": "#f0fdfa",
    "teal-100": "#ccfbf1",
    "teal-200": "#99f6e4",
    "teal-300": "#5eead4",
    "teal-400": "#2dd4bf",
    "teal-500": "#14b8a6",
    "teal-600": "#0d9488",
    "teal-700": "#0f766e",
    "teal-800": "#115e59",
    "teal-900": "#134e4a",
    "sky-50": "#f0f9ff",
    "sky-100": "#e0f2fe",
    "sky-200": "#bae6fd",
    "sky-300": "#7dd3fc",
    "sky-400": "#38bdf8",
    "sky-500": "#0ea5e9",
    "sky-600": "#0284c7",
    "sky-700": "#0369a1",
    "sky-800": "#075985",
    "sky-900": "#0c4a6e",
    "blue-50": "#eff6ff",
    "blue-100": "#dbeafe",
    "blue-200": "#bfdbfe",
    "blue-300": "#93c5fd",
    "blue-400": "#60a5fa",
    "blue-500": "#3b82f6",
    "blue-600": "#2563eb",
    "blue-700": "#1d4ed8",
    "blue-800": "#1e40af",
    "blue-900": "#1e3a8a",
    "indigo-50": "#eef2ff",
    "indigo-100": "#e0e7ff",
    "indigo-200": "#c7d2fe",
    "indigo-300": "#a5b4fc",
    "indigo-400": "#818cf8",
    "indigo-500": "#6366f1",
    "indigo-600": "#4f46e5",
    "indigo-700": "#4338ca",
    "indigo-800": "#3730a3",
    "indigo-900": "#312e81",
    "purple-50": "#f5f3ff",
    "purple-100": "#ede9fe",
    "purple-200": "#ddd6fe",
    "purple-300": "#c4b5fd",
    "purple-400": "#a78bfa",
    "purple-500": "#8b5cf6",
    "purple-600": "#7c3aed",
    "purple-700": "#6d28d9",
    "purple-800": "#5b21b6",
    "purple-900": "#4c1d95",
    "pink-50": "#fdf2f8",
    "pink-100": "#fce7f3",
    "pink-200": "#fbcfe8",
    "pink-300": "#f9a8d4",
    "pink-400": "#f472b6",
    "pink-500": "#ec4899",
    "pink-600": "#db2777",
    "pink-700": "#be185d",
    "pink-800": "#9d174d",
    "pink-900": "#831843",
}


def text_font(size):
    return ("Lilita One", size)


btn_font = ("Lilita One", 18)
btn_hover_color = (colors["gray-300"], colors["gray-700"])
btn_text_color = (colors["neutral-900"], colors["gray-50"])
scroll_btn_color = (colors["neutral-300"], colors["gray-500"])
scroll_hover_color = (colors["neutral-800"], colors["gray-300"])
input_text_color = colors["neutral-900"]
frame_radius = 10


def create_back_button(parent, command):
    return CTkButton(
        master=parent,
        command=command,
        fg_color=colors["gray-700"],
        hover_color=colors["gray-800"],
        text_color=colors["gray-50"],
        text="Back",
        font=btn_font,
    )


def update(widget, index, value):
    widget.configure(state="normal")
    widget.delete(index, "end")
    widget.insert(index, value)


def textbox_update(textbox, value):
    update(textbox, "0.0", value)
    textbox.configure(state="disabled")


def entry_update(entry, value):
    update(entry, 0, value)
    entry.configure(state="readonly")


def create_frame_title(parent, title):
    label = CTkLabel(
        parent,
        text=title,
        font=text_font(26),
        text_color=colors["gray-200"],
        fg_color=colors["sky-700"],
        corner_radius=frame_radius,
        bg_color="transparent",
    )
    label.grid(row=0, column=0, sticky="ew", ipady=10)
    return label
