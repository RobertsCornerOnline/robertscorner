#!/usr/bin/env python3
"""Download every image the site uses from robscornerr.wordpress.com into ./images/.
Run once from the site folder:   python3 download_images.py
Safe to re-run: files that already exist are skipped."""
import os, urllib.request
FILES = [
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/08/img_20250330_205521__2_-removebg.png",
  "images/profile.png"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/12/wp-17352711099843869233862435577947.jpg",
  "images/photographs/01-forest-tower.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/12/wp-17352711115957591371293586769097.jpg",
  "images/photographs/02-cloud-light.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/12/wp-17352711147507888524005759232129.jpg",
  "images/photographs/03-curious.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/12/wp-17352711109907429261842101734327.jpg",
  "images/photographs/04-sunset-afterglow.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/12/wp-1735271118406572939670682561195.jpg",
  "images/photographs/05-campfire.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/12/wp-17352711177595229960977857861452.jpg",
  "images/photographs/06-chennai-lighthouse.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/12/wp-17352711194043265611714439824302.jpg",
  "images/photographs/07-tech-detox.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/12/wp-17352711159627758193653764865644.jpg",
  "images/photographs/08-city-nights.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/12/wp-17352711139322953778149671665588.jpg",
  "images/photographs/09-pond-flowers.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/12/wp-17352711123154028537387618218659.jpg",
  "images/photographs/10-bird-rainbow.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/06/img_20240607_1529195501150118967621720.jpg",
  "images/myself/01.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/08/img_20240607_1526507838442921350790981.jpg",
  "images/myself/02.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/08/img_20240527_184408-15012941219878523113.jpg",
  "images/myself/03.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/08/img_20240607_1502302370180193784382824.jpg",
  "images/myself/04.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/08/whatsapp-image-2024-03-30-at-5.21.37-pm-2.jpeg",
  "images/myself/05.jpeg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/08/img-20240428-wa00252660694760283511424.jpg",
  "images/myself/06.jpg"
 ],
 [
  "https://robscornerr.wordpress.com/wp-content/uploads/2024/08/whatsapp-image-2024-03-30-at-5.17.51-pm.jpeg",
  "images/myself/07.jpeg"
 ]
]
here = os.path.dirname(os.path.abspath(__file__))
ok = bad = 0
for url, rel in FILES:
    dest = os.path.join(here, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print("skip  ", rel); continue
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
            f.write(r.read())
        print("saved ", rel); ok += 1
    except Exception as e:
        print("FAILED", rel, "-", e); bad += 1
print(f"\nDone: {ok} saved, {bad} failed.")
