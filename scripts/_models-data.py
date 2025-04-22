## MODEL
model_list = {
    "1. Meina-Mix [Anime] [V12] + INP": [
        {'url': "https://civitai.com/api/download/models/948574", 'name': "MeinaMix_V12.safetensors"}
    ],
    "2. Mix-Pro [Anime] [V4] + INP": [
        {'url': "https://huggingface.co/fp16-guy/MIX-Pro-V4_fp16_cleaned/resolve/main/mixProV4_v4_fp16.safetensors", 'name': "MixPro_V4.safetensors"},
        {'url': "https://huggingface.co/fp16-guy/MIX-Pro-V4_fp16_cleaned/resolve/main/mixProV4_v4_inp_fp16.safetensors", 'name': "MixPro_V4-inpainting.safetensors"},
        {'url': "https://huggingface.co/fp16-guy/MIX-Pro-V4.5_fp16_cleaned/resolve/main/mixProV45Colorbox_v45_fp16.safetensors", 'name': "MixPro_V4_5.safetensors"},
        {'url': "https://huggingface.co/fp16-guy/MIX-Pro-V4.5_fp16_cleaned/resolve/main/mixProV45Colorbox_v45_inp_fp16.safetensors", 'name': "MixPro_V4_5-inpainting.safetensors"}
    ],
    "3. Hassaku-XL Illustrious V2.1 FIX": [
        {'url': "https://civitai.com/api/download/models/140272", 'name': "Hassaku-XL-Illustrious.safetensors"}
    ],
}

## VAE

vae_list = {
    "1. Anime.vae": [
        {'url': "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/kl-f8-anime2_fp16.safetensors", 'name': "Anime-kl-f8.vae.safetensors"},
        {'url': "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/vae-ft-mse-840000-ema-pruned_fp16.safetensors", 'name': "Anime-mse.vae.safetensors"}
    ],
    "2. Anything.vae": [{'url': "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/anything_fp16.safetensors", 'name': "Anything.vae.safetensors"}],
    "3. Blessed2.vae": [{'url': "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/blessed2_fp16.safetensors", 'name': "Blessed2.vae.safetensors"}],
    "4. ClearVae.vae": [{'url': "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/ClearVAE_V2.3_fp16.safetensors", 'name': "ClearVae_23.vae.safetensors"}],
    "5. WD.vae": [{'url': "https://huggingface.co/NoCrypt/resources/resolve/main/VAE/wd.vae.safetensors", 'name': "WD.vae.safetensors"}]
}

## CONTROLNET

controlnet_list = {
    "1. Openpose": [
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose_fp16.safetensors"},
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_openpose_fp16.yaml"}
    ],
    "2. Canny": [
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors"},
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_canny_fp16.yaml"}
    ],
    "3. Depth": [
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors"},
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1p_sd15_depth_fp16.yaml"}
    ],
    "4. Lineart": [
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart_fp16.safetensors"},
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_lineart_fp16.yaml"},
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors"},
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15s2_lineart_anime_fp16.yaml"}
    ],
    "5. ip2p": [
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors"},
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_ip2p_fp16.yaml"}
    ],
    "6. Shuffle": [
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors"},
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_shuffle_fp16.yaml"}
    ],
    "7. Inpaint": [
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors"},
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_inpaint_fp16.yaml"}
    ],
    "8. Scribble": [
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble_fp16.safetensors"},
        {'url': "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_scribble_fp16.yaml"}
    ]
}

## LORA
lora_list = {
    "1. Detail Tweaker LoRA": [
        {'url': "https://civitai.com/api/download/models/58390", 'name': "detail_tweaker.safetensors"}
    ],
    "2. Add More Details LoRA": [
        {'url': "https://civitai.com/api/download/models/87153", 'name': "add_more_details.safetensors"}
    ]
    # Add more SD 1.5 LoRAs here
}