from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

import os
TOKEN = os.getenv("TOKEN")

# ======================
# MENU UTAMA
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("BELI SATUAN", callback_data="menu_ml")],
        [InlineKeyboardButton("BELI 1-5 GRUB (LEBIH MURAH)", callback_data="menu_ff")]
    ]

    await update.message.reply_text(
        "👋 Selamat datang di toko GRUB VVIP PREMIUM. Join Channel ini untuk cek testimoni -> https://t.me/+YZ6WYwfsTINiNTk1 . NOTE = SETELAH LAKUKAN PEMBAYARAN LANGSUNG KONFIRMASI DENGAN CARA KIRIM BUKTI TRANSFER KE @Ownervviptrusted\nPilih kategori:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ======================
# HANDLE TOMBOL
# ======================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    qris = "qris.png"

    # ======================
    # MENU BELI SATUAN (9 MENU)
    # ======================
    if query.data == "menu_ml":
        keyboard = [
            [InlineKeyboardButton("🔥 INDO LOKAL - 50K", callback_data="ml_1")],
            [InlineKeyboardButton("🔥 BOCIL LOKAL - 50K", callback_data="ml_2")],
            [InlineKeyboardButton("🔥 TOBRUT LOKAL - 50K", callback_data="ml_3")],
            [InlineKeyboardButton("🔥 INDONESIA VIRAL - 100K", callback_data="ml_4")],
            [InlineKeyboardButton("🔥 INDONESIA KING - 100K", callback_data="ml_5")],
            [InlineKeyboardButton("🔥 VIRAL TERBARU - 100K", callback_data="ml_6")],
            [InlineKeyboardButton("🔥 PEMERKOSAAN - 100K", callback_data="ml_7")],
            [InlineKeyboardButton("🔥 JAV SUB INDO - 100K", callback_data="ml_8")],
            [InlineKeyboardButton("🔥 REMAJA SMK - 100K", callback_data="ml_9")],
            [InlineKeyboardButton("⬅️ Kembali", callback_data="back")]
        ]

        await query.message.edit_text(
            "📦 BELI SATUAN\nPilih produk:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================
    # MENU PAKET
    # ======================
    elif query.data == "menu_ff":
        keyboard = [
            [InlineKeyboardButton("🔥 2 GRUB LOKAL - 75K", callback_data="ff_1")],
            [InlineKeyboardButton("🔥 ALL GRUB LOKAL - 100K", callback_data="ff_2")],
            [InlineKeyboardButton("🔥 8 GRUB (100K) - 350K", callback_data="ff_3")],
            [InlineKeyboardButton("🔥 15 GRUB (100K) - 400K", callback_data="ff_4")],
            [InlineKeyboardButton("🎁 ALL GRUB (100K) - 600K", callback_data="ff_5")],
            [InlineKeyboardButton("⬅️ Kembali", callback_data="back")]
        ]

        await query.message.edit_text(
            "📦 BELI PAKET GRUB\nPilih paket:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================
    # PRODUK SATUAN (UPDATED)
    # ======================
    elif query.data.startswith("ml_"):
        if not os.path.exists(qris):
            await query.message.reply_text("❌ File qris.png tidak ditemukan!")
            return

        produk = {
            "ml_1": "🔥 INDO LOKAL\n💰 Rp50.000",
            "ml_2": "🔥 BOCIL LOKAL\n💰 Rp50.000",
            "ml_3": "🔥 TOBRUT LOKAL\n💰 Rp50.000",
            "ml_4": "🔥 INDONESIA VIRAL\n💰 Rp100.000",
            "ml_5": "🔥 INDONESIA KING\n💰 Rp100.000",
            "ml_6": "🔥 VIRAL TERBARU\n💰 Rp100.000",
            "ml_7": "🔥 PEMERKOSAAN\n💰 Rp100.000",
            "ml_8": "🔥 JAV SUB INDO\n💰 Rp100.000",
            "ml_9": "🔥 REMAJA SMK\n💰 Rp100.000"
        }

        await query.message.reply_photo(
            photo=open(qris, "rb"),
            caption=f"{produk[query.data]}\n\n📌 Scan QRIS untuk pembayaran\n\n📩 Kirim bukti transfer ke @Ownervviptrusted"
        )

    # ======================
    # PRODUK PAKET
    # ======================
    elif query.data.startswith("ff_"):
        if not os.path.exists(qris):
            await query.message.reply_text("❌ File qris.png tidak ditemukan!")
            return

        produk = {
            "ff_1": "🔥 2 GRUB LOKAL\n💰 Rp75.000",
            "ff_2": "🔥 ALL GRUB LOKAL\n💰 Rp100.000",
            "ff_3": "🔥 8 GRUB (100K)\n💰 Rp350.000",
            "ff_4": "🔥 15 GRUB (100K)\n💰 Rp400.000",
            "ff_5": "🔥 ALL GRUB (100K)\n💰 Rp600.000"
        }

        await query.message.reply_photo(
            photo=open(qris, "rb"),
            caption=f"{produk[query.data]}\n\n📌 Scan QRIS untuk pembayaran\n\n📩 Kirim bukti transfer ke @Ownervviptrusted"
        )

    # ======================
    # KEMBALI
    # ======================
    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("BELI SATUAN", callback_data="menu_ml")],
            [InlineKeyboardButton("BELI 1-5 GRUB (LEBIH MURAH)", callback_data="menu_ff")]
        ]

        await query.message.edit_text(
            "👋 Pilih kategori:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# ======================
# RUN BOT
# ======================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()