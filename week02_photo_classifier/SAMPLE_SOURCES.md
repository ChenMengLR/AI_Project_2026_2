# 第2周课堂样例来源

这五张图片与教师讲义中的样例相同，下载日期为2026年9月17日。预期标签来自讲义，实际分类须运行Qwen后确认。

课程原文：https://app.notion.com/p/3cf7c00fe5ad8140b175c415d1613a7e

- sample-01.jpg：预期 person；原图来源 https://unsplash.com/photos/grayscale-picture-of-persons-portrait-NlHGKAZ3jCI；尺寸 3600×3600。
- sample-02.jpg：预期 document；原图来源 https://unsplash.com/photos/a-close-up-of-a-stack-of-papers-3CLPBgNuX40；尺寸 3600×2394。
- sample-03.jpg：预期 food；原图来源 https://unsplash.com/photos/a-plate-of-food-DBVIb_rWUKw；尺寸 3600×2400。
- sample-04.jpg：预期 device；原图来源 https://unsplash.com/photos/a-laptop-on-a-desk-FV6Pma5U_98；尺寸 3600×2400。
- sample-05.jpg：预期 other；原图来源 https://unsplash.com/photos/forest-trees-jFCViYFYcus；尺寸 3600×2398。

上述五张图片按讲义链接对应的 Unsplash 资源下载为 JPEG，未修改图像内容。是否完成 API 调用以 `runtime/last_run.json` 的真实运行记录为准。

## 本次新增的两张测试图片

以下素材于 2026-09-17 由助手为课程个人实践补充，都是公开授权照片，不是 WANG HAOBIN 本人拍摄。两张原文件保持未修改；预期类别用于运行后的人工核对，不能代替模型实际返回。

- `new-01-apples.jpg`：预期 `food`；Scott Bauer / U.S. Department of Agriculture；来源页：[Red apple fruits](https://commons.wikimedia.org/wiki/File:Red_apple_fruits.jpg)，来源页标明作者将作品置于公共领域；原图 2790 × 1758。
  SHA-256：`1cbbb9b96b91e28e63263c757b3c9f40712826c0c004a89f36b56a0c4583af78`。
- `new-02-keyboard.jpg`：预期 `device`；作者 Samiknoov；来源页：[Black Computer keyboard](https://commons.wikimedia.org/wiki/File:Black_Computer_keyboard.jpg)，许可为 [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)；原图 4000 × 3000。
  SHA-256：`a022cf70e99c32fa73a7e5ade49bf0118f7cfd0f60b215c11848029d75e5502b`。

当前 `input/` 共 7 张照片，包含 5 张教师样例和 2 张新素材。如果教师要求必须本人拍摄，可再用本人照片替换两张新增素材并重新分类；不得把公开素材标注为本人摄影。
